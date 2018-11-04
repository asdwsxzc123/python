from socket import *
# import socket

def main():
  udp_socket = socket(AF_INET, SOCK_DGRAM)

  # 绑定端口
  local_addr = ('', 7788) #ip地址和端口号,ip可以不用写,表示本机的任何一个ip
  udp_socket.bind(local_addr)

  # 接收数据
  recv_data = udp_socket.recvfrom(1024) 
  print(recv_data[0].decode('gbk')) # 接收数据
  print(recv_data[1]) #接收的地址

  # dest_addr = ('196.168.43.153',8080)
  # while True:
  #   send_data = input('请输入要发送的数据:')
  #   if send_data == 'exit':
  #     break
  #   # udp_socket.sendto(b'hahaha', dest_addr)
  #   udp_socket.sendto(send_data.encode('utf-8'), dest_addr)
  udp_socket.close()

if __name__ == '__main__':
  main()
