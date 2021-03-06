import multiprocessing
import socket
import re
import sys
class WSGIServer(object):
    def __init__(self, port,app, static):
        self.application = app
        self.static_path = static
        # 1. 创建套接字
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 握手问题
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        print('listen: %s' %port)
        # 2. 绑定,端口
        self.tcp_server_socket.bind(('', port))
        # 3. 监听套接字
        self.tcp_server_socket.listen(128)

    def service_client(self,new_socket):
        request = new_socket.recv(1024).decode('utf-8')
        request_lines = request.splitlines()
        print(request_lines)
        # GET /INDEX.HTML HTTP/1.1 200 OK
        file_name = ''
        ret = re.match(r'[^/]+(/[^ ]*)', request_lines[0])
        if ret:
            file_name = ret.group(1)
            if file_name == '/':
                file_name = '/index.html'

        # 返回http格式的数据,给浏览器
        # 如果请求的不是一.py结尾的,认为是静态资源
        if not file_name.endswith('.py'):
            try:
                f = open(self.static_path + file_name, 'rb')
            except Exception as ret:
                respone = 'HTTP/1.1 404 NOT FOUNT\r\n'
                respone += '\r\n'
                respone += 'file is not found'
                new_socket.send(respone.encode('utf-8'))
            else:
                content_html = f.read()
                f.close()
                respone = 'HTTP/1.1 200 OK\r\n'
                respone += '\r\n'
                # 将header 发送给服务器
                new_socket.send(respone.encode('utf-8'))
                # 将body 发送给服务器
                new_socket.send(content_html)
        else: 
            env = dict()
            env['PATH_INFO'] = file_name
            body = self.application(env, self.set_response_header)
            # body = mini_frame.application(env, self.set_response_header)
            # .py格式
            header = 'HTTP/1.1 %s\r\n'%self.status
            for temp in self.headers:
                header += '%s:%s\r\n' %(temp[0],temp[1])

            header += '\r\n'
            respone = header + body
            
            new_socket.send(respone.encode('utf-8'))
        # 关闭套链
        new_socket.close()
    def set_response_header(self,status,headers):
        self.status = status
        self.headers = [('server', 'BWS/1.0')]
        self.headers += headers
    def runforever(self):
        while True:
            # 等待新客户端的链接
            new_socket, clientAddr = self.tcp_server_socket.accept()
            # 5. 为这个服务端服务子进程会覆盖
            p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
            p.start()
            # 主进程和子进程都有一份标记,因此在主进程也需要关闭
            new_socket.close()
        # 关闭套接字
        self.tcp_server_socket.close()


def main():
    # 控制整体,创建一个web服务器对象,然后调用这个run_forever方法
    # 给程序添加参数
    if len(sys.argv) == 3:
        try:
            port = int(sys.argv[1])
            frame_app_name = sys.argv[2]
        except Exception as ret:
            print('端口输入错误')
            return
    else:
        print('请按照以下方式运行')
        print('python3 xxx.py 7890 mini_frame:application')
        return
    ret = re.match(r'([^:]+):(.*)', frame_app_name)
    if ret:
        frame_name = ret.group(1)
        app_name = ret.group(2)
    else:
        print('请按照以下方式运行')
        print('python3 xxx.py 7890 mini_frame:application')
        return


    with open('./web_server.conf') as f:
        # 这个字典类型
        conf_info = eval(f.read())
        print(conf_info)
        
        
    sys.path.append(conf_info['dynamic_path'])
    frame = __import__(frame_name) # 返回值标记这个 导入的模块
    print(frame)
    app = getattr(frame, app_name)
    wsgi_server = WSGIServer(port,app,conf_info['static'])
    wsgi_server.runforever()

if __name__ == "__main__":
    main()
