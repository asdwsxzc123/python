# 不需要写服务器的信息,写自己框架的信息
def application(environ, start_response):
    start_response(
        '200 OK', [('Content-type', 'text/html;charset=utf-8')])
    return 'hello world,中国'
