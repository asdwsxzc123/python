import socket


def send_msg(udp_socket):
   # 发送
    dest_ip = '192.168.220.1'
    dest_port = 8080
    send_data = input('请输入要发送的消息:')
    # dest_port = int(input('请输入对方的port:'))
    # send_data = input('请输入要发送的消息:')
    udp_socket.sendto(send_data.encode('gbk'), (dest_ip,dest_port))


def recv_msg(udp_socket):
  # 接收并显示
    recv_data = udp_socket.recvfrom(1024)
    print('%s:%s' % (str(recv_data[1]), recv_data[0].decode('utf-8')))

def main():
  # 创建套接字
  udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  udp_socket.bind(('192.168.220.136', 7788))
  # udp_addr = ('192.168.')
  while True:
    print('==聊天器===')
    print('1:发送信息')
    print('2:接收信息')
    print('0:退出系统')
    num = int(input('请输入功能:'))
    if num == 1:
      send_msg(udp_socket)
    elif num == 2:
      recv_msg(udp_socket)
    elif num == 0:
      exit()
      
    
if __name__ == '__main__':
  main()
