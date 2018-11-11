# tcp三次握手 数据传输 4次挥手
# 全双工的,有两个通道,接收和发送通道
  # 第一次握手
  # 1. C告诉S我准备好链接你 connet,发个值给S syn 11
  # 第二次握手
  # 2. S告诉C我也准备好了,S吧值加1给C,并主动发了一个值给C ack12 syn44
  # 第三次握手
  # 3. C收到S的的值,知道S准备好了,并告知S我收到了 ack45

# 关闭
# 谁先调用close,谁需要等待2-5分钟,才能释放资源
  # 一般是客户端先关
  # 1. C告诉 S,我要关闭了,close(),关闭发
  # 2. S 收到后,告诉 c我知道了
    # recv_data = new_socket.recv()
    # if recv_data: pass
  # 3. S 告诉 C 我关闭了,有个超时时间,如果c没有回,会再次发,告诉c我关闭了
    # else: new_socket.close()
  # 4. C收到后,告诉 S, 我收到了 C关闭发
from socket import *
def service_client(new_socket):
  # 接收到的数据
    new_socket.recv(1024)
    # 响应头header
    response = 'HTTP/1.1 200 OK\r\n'
    response += '\r\n'
    # 响应主题body
    response += '<h1>hello world</h1>'
    # 发送信息并转码
    new_socket.send(response.encode('utf-8'))

    new_socket.close()


def main():
  # 创建套接字
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    tcp_server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    # 绑定端口,注意是元组
    tcp_server_socket.bind(('', 7788))
    # 监听的个数
    tcp_server_socket.listen(128)
    while True:
      # 等待回复
        new_socket, clientAddr = tcp_server_socket.accept()
        print(clientAddr)
        # 创建服务端
        service_client(new_socket)
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
