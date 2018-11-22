def index():
    return '主页'
def login():
    return '登录'
    

def application(environ, start_response):
# 不需要写服务器的信息,写自己框架的信息
    start_response(
        '200 OK', [('Content-type', 'text/html;charset=utf-8')])
    if environ['PATH_INFO'] == '/index.py':
        return index()
    elif environ['PATH_INFO'] == '/login.py':
        return login()
    else:
        return 'hallo world'