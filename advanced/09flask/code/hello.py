# codind:utf-8
from flask  import Flask

# 创建flask的应用
# __name__表示当前的模块名称
#   模块名,flask以这个模块所在的目录为总目录,默认这个目录中的static为静态目录,templates为模板目录
app = Flask(__name__)

@app.route('/')
def index():
    # 定义视图函数
    return 'hello world'

if __name__ == "__main__":
    app.run()