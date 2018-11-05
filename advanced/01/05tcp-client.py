from socket import *
def main():

  # 创建套接字
  tcp_client_socket = socket(AF_INET, SOCK_STREAM)

  server_ip = input('请输入ip:')

  server_port = int(input('请输入端口:'))
  # 创建连接
  tcp_client_socket.connect((server_ip, port))
  send_data = input('请输入要发送的数据:')

  # 发送信息
  tcp_client_socket.send(send_data.encode('utf-8'))

  # 接收信息

  # 关闭服务器
  tcp_client_socket.close(
if __name__ == '__main__':
	main()

