# 1.短连接
# 建立连接-数据传输--关闭链接

# 2. 长连接 游戏都是长连接
# 建立连接--数据传输 多次数据传输
from socket import *
import re
import time


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
    print('-'*50)
    print(response)
    new_socket.send(response.encode('utf-8'))
  else:
    content_html = f.read()
    print('='*50)
    print(content_html)

    f.close()
    response_body = content_html
    response_header = 'HTTP/1.1 200 OK\r\n'
    # 当写了长度后,可以使用长连接
    response_header += 'Content-Length:%d\r\n'% len(response_body)
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
  client_socket_list = list()
  while True:
    try:
      new_socket, clientAddr = tcp_server_socket.accept()
    except Exception as ret:
      pass
    else:
      new_socket.setblocking(False)  # 设置套接字为非阻塞模式
      client_socket_list.append(new_socket)

      for client_socket in client_socket_list:
        try:
          recv_data = client_socket.recv(1024).decode('utf-8')
        except Exception as ret:
          print(ret)
        else:
          if recv_data:
            service_client(new_socket, recv_data)
          else:
            client_socket.close()
            client_socket_list.remove(client_socket)

  tcp_server_socket.close()


if __name__ == "__main__":
    main()
