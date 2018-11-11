# io 多路复用
# epoll io方式 event driven IO kernel
# 特点: 1.事件通知 2.共享内存空间(内存映射mmap)
# 普通的线程问题,需要遍历,占内存
# 而io(kernel操作系统内核),使用一个独立的内存空间,将数据共享给服务器和内核,不遍历(轮询),以事件通知的方式来监听,谁触发事件,执行谁
""" 轮询和事件通知 """
# epoll的好处在于单个
import select
import re
from socket import *


def service_client(new_socket, request):
  print(request)
  request_lines = request.splitlines()

  # GET /INDEX.HTML HTTP/1.1 200 OK
  file_name = ''
  ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
  if ret:
    file_name = ret.group(1)
    if file_name == '/':
      file_name = '/index.html'

  try:
    f = open('./html' + file_name, 'rb')
  except Exception as ret:
    response = 'HTTP/1.1 404 NOT FOUNT\r\n'
    response += '\r\n'
    response += 'file is not found'
    new_socket.send(response.encode('utf-8'))
  else:
    content_html = f.read()

    f.close()
    response_body = content_html
    response_header = 'HTTP/1.1 200 OK\r\n'
    # 当写了长度后,可以使用长连接
    response_header += 'Content-Length:%d\r\n' % len(response_body)
    response_header += '\r\n'
    response = response_header.encode('utf-8') + response_body
    new_socket.send(response)

  # new_socket.close()


def main():
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    tcp_server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    tcp_server_socket.bind(('', 7788))
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)
    # 创建一个epoll
    epl = select.epoll()
    # 将监听套接字对应的文件描述符fd注册到epoll中
    epl.register(tcp_server_socket.fileno(), select.EPOLLIN)
    fd_event_dict = dict()
    client_socket_list = list()
    while True:
        # 默认会堵塞,知道os检测到数据到来,通过事件通知通知方式,告诉程序,此时才会解堵塞
        fd_event_list = epl.poll()
        # 第一次解阻塞一定是可以收数据了
        # [(fd,event) ,套接字对应的文件描述符,事件类型]
        for fd, event in fd_event_list:
            print(fd, event)
            if fd == tcp_server_socket.fileno():
                new_socket, clientAddr = tcp_server_socket.accept()
                epl.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                recv_data = fd_event_dict[fd].recv(1024).decode('utf-8')
                if recv_data:
                  service_client(fd_event_dict[fd],recv_data)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]

    tcp_server_socket.close()


if __name__ == "__main__":
    main()
