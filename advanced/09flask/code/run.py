# codind:utf-8
from flask  import Flask


# 创建flask的应用
# __name__表示当前的模块名称
#   模块名,flask以这个模块所在的目录为总目录,默认这个目录中的static为静态目录,templates为模板目录

# app初始化参数
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

# 配置参数的使用
app.config.from_pyfile('config.cfg')



@app.route('/')
def index():
    # 定义视图函数
    return 'hello world'

if __name__ == "__main__":
    app.run(host='192.168.220.138',port=7788)
