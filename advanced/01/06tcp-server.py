# tcp服务器
# 1.socket创建一套接字
# 2. bind绑定ip和port
# 3. listen 使套接字变为可以被动链接
# 4. accept等待客户端的链接
# 5. recv/send接受发送数据
from socket import *


def main():

    # 创建socket
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)

    address = ('', 7788)
    # 绑定
    tcp_server_socket.bind(address)
    print('listen')
    # listen将其变为被动,可以接受别人的链接
    tcp_server_socket.listen(128)
    while True:
        # 等待客户端的链接,accept
        client_socket, clientAddr = tcp_server_socket.accept()
        print('accept')

        print(clientAddr)
        # 先收数据
        recv_data = client_socket.recv(1024)
        print('客户数据:%s' % recv_data.decode('utf-8'))
        # 再发数据
        client_socket.send('haha'.encode('utf-8'))
        client_socket.close()
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
