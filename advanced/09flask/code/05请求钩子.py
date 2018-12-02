# hook
# 请求钩子是通过装饰器的形式实现,flask支持以下4种钩子
# before_first_request: 在处理第一次请求前运行
# @app.before_first_request

# before_request 每次请求前运行

# after_request(response) 如果没有未处理的异常抛出,每次请求之后

# teardown_request(response) 请求后执行,及时有抛出异常