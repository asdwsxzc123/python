from socket import *
import re
import time

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
      print('---没有新的客户端到来---')
    else:
      print('--来了一个新的客户端--')
      new_socket.setblocking(False) #设置套接字为非阻塞模式
      client_socket_list.append(new_socket)

      for client_socket in client_socket_list:
        try:
          recv_data = client_socket.recv(1024)
        except Exception as ret:
          print('---客户端没有发送数据过来---')
          print(ret)
        else:
          if recv_data:
            print('---客户端发送了数据---')
          else :
            client_socket_list.remove(client_socket)
            client_socket.close()
    time.sleep(1)

  tcp_server_socket.close()


if __name__ == "__main__":
    main()
