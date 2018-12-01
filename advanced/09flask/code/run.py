# codind:utf-8
from flask  import Flask,current_app,redirect, url_for
from werkzeug.routing import BaseConverter

# 创建flask的应用
# __name__表示当前的模块名称
#   模块名,flask以这个模块所在的目录为总目录,默认这个目录中的static为静态目录,templates为模板目录

""" app初始化参数 """
# import_name: 导入路径(寻找静态目录与模板目录位置的参数)
# static_url_path:
# static_folder
# template_folder
app = Flask(
    __name__,
    static_url_path='/python', # 访问静态资源的url前缀,默认值是static
    static_folder='static',  # 静态文件的目录,默认值是static
    template_folder='templates'  # 静态模板文件的目录,默认值是templates
)

""" 配置参数的使用 """
# 1.使用配置文件
# app.config.from_pyfile('config.cfg')

# 2.使用对象添加配置参数
class Config(object):
    DEBUG = True
    STATIC = 'python'
app.config.from_object(Config)

# 3.直接操作config字典对象
# app.config['DEBUG'] = True

""" 路由的使用 """
@app.route('/')
def index():
    # 定义视图函数
    
    """ 读取config参数 """
    # 1.从app全局对象直接获取
    # print(app.config.get('STATIC'))
    # 2.current_app
    # print(current_app.config.get('STATIC'))
    return 'hello world'

# 通过methods限定访问方式
@app.route('/post_only', methods=['POST'])
def post_only():
    return 'post only page'

@app.route('/hello', methods=['POST'])
def hello():
    return 'hello 1'

@app.route('/hello', methods=['GET'])
def hello2():
    return 'hello 2'

@app.route('/hi1')
@app.route('/hi2')
def hi():
    return 'hi'

# 路由重定向
# urls = [
#     url(r'/index', index, name="index_view")
# ]
# redirect(reverse_url('index_view'))

""" 路由重定向 """
@app.route('/login')
def login():
    # url = '/'
    # 使用url_for函数,通过视图函数的名字找到视图对应的url路径
    url = url_for('index')
    return redirect(url)

@app.route('/register')
def register():
    # 使用url_for函数,通过视图函数的名字找到视图对应的url路径
    url = url_for('index')
    return redirect(url)

""" 路由传参 """
# <>加转换器类型
@app.route('/goods/<int:id>')
def goods(id):
    return 'id: %d' % id

# 不加转换器,直接传参,默认是字符串
@app.route('/good_str/<id>')
def good_str(id):
    return 'id: %s' % id

""" 自定义转化器 """
# 1. 定义自己的转换器
class MobileConverter(BaseConverter):
    def __init__(self,url_map):
        super(MobileConverter,self).__init__(url_map)
        self.regex = r"1[34578]\d{9}"
class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        # 调用父类的初始化方法
        super(RegexConverter, self).__init__(url_map)
        # 将正则表达式的参数保存到对象的属性中,flask去使用这个属性来进行路由的正则匹配
        self.regex = regex
    # 可以拦截正则获取的值,可以做类型转换
    def to_python(self, value):
        print('to_python被调用')
        return '123'
    # 吧视图中python的数据放到url中
    def to_url(self, value):
        print('调用to_url')
        return value

# 2. 将自定义的转换器添加到flask的应用中
app.url_map.converters['re'] = RegexConverter
app.url_map.converters['mobile'] = MobileConverter

# @app.route('/send/<mobile:mobile_num>')
@app.route('/send/<re(r"1[34578]\d{9}"):mobile_num>')
def send_sms(mobile_num):
    return 'send sms to %s' % mobile_num

@app.route('/index1')
def index1():
    # /send/
    url = url_for('send_sms', mobile_num='18102216679')
    return redirect(url)

if __name__ == "__main__":
    # 通过该url_map可以查看整个flask中的路由信息
    print(app.url_map)
    app.run(host='0.0.0.0',port=7788)
