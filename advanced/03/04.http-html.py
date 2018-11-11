from socket import *
import re
def service_client(new_socket):
  request = new_socket.recv(1024).decode('utf-8')
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
  except Exception as ret :
    respone = 'HTTP/1.1 404 NOT FOUNT\r\n'
    respone += '\r\n'
    respone += 'file is not found'
    new_socket.send(respone.encode('utf-8'))
  else:
    content_html = f.read()
    f.close()
    respone = 'HTTP/1.1 200 OK\r\n'
    respone += '\r\n'
    new_socket.send(respone.encode('utf-8'))
    new_socket.send(content_html)
  new_socket.close()

def main():
  tcp_server_socket = socket(AF_INET, SOCK_STREAM)
  tcp_server_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
  tcp_server_socket.bind(('',7788))
  tcp_server_socket.listen(128)
  while True:
    new_socket, clientAddr = tcp_server_socket.accept()
    service_client(new_socket)
if __name__ == "__main__":
    main()
