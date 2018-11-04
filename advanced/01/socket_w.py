from socket import *
# import socket


def main():
  udp_socket = socket(AF_INET, SOCK_DGRAM)
  dest_addr = ('127.0.0.1',8080)
  while True:
    send_data = input('请输入要发送的数据:')
    if send_data == 'exit':
      break
    # udp_socket.sendto(b'hahaha', dest_addr)
    udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
  udp_socket.close()


if __name__ == '__main__':
  main()
