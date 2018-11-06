# 文件下载
from socket import *

def main():
  tcp_socket = socket(AF_INET,SOCK_STREAM)
  ip = '192.168.220.1'
  port = 8080
  addre = (ip,port)
  tcp_socket.connect(addre)
  download_file_name = input('请输入要下载的文件名字:')
  tcp_socket.send(download_file_name.encode('utf-8'))
  recv_data = tcp_socket.recv(1024*1024)
  with open('[附件]'+download_file_name, 'wb') as f:
    f.write(recv_data)
  tcp_socket.close()
  
if __name__ == '__main__':
  main()