from socket import *


def send_file_2_client(tcp_client_socket, clientAddr):
  #  接收客户端发送过阿里的要下载的文件名
  file_name = tcp_client_socket.recv(1024).decode('utf-8')
  print('客户端%s需要下载的文件:%s' % (clientAddr, file_name))
  file_content = None
  # 打开文件,读取文件
  try:
    f=open(file_name,'rb')
    file_content = f.read()
    print(file_content)
    f.close()
  except Exception as ret:
    print('没有要下载的文件:%s'%file_name)
  if file_content:
    with open('[新]' + file_name, 'wb') as f:
        f.write(file_content)

def main ():
  tcp_server = socket(AF_INET,SOCK_STREAM)
  port = 7788
  # 服务端的端口
  tcp_server.bind(('', port))
  # 128是指的服务端连接的个数
  tcp_server.listen(128)
  print('监听端口:%s' % port)
  # 接收数据
  (tcp_client_socket, clientAddr) = tcp_server.accept()
  
  send_file_2_client(tcp_client_socket, clientAddr)
  
  #关闭服务
  tcp_client_socket.close()
  tcp_server.close()
  


if __name__ == '__main__':
  main()
