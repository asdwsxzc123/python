# xx: 共有变量
# _x: 前置单下划线,私有化属性或方法,from module import *禁止导入,类的对象和资料可以访问
# __xx: 双前置下划线,避免与子类中的属性命名冲突,无法在再外部直接访问(私有化)
# __xx__: 用户名称空间的魔法对象和属性,不要自己发明
# xx_: 单后置下划线,用于避免与python关键字冲突

# 私有化的目的,为了不让别人使用这个变量

""" import """
# from xxx import yyy 定义了一个变量叫yyy,指向的是值
# import xxx #模块
# import xxx #模块
# from xxx import *
# import xxx as xxx

# 模块导入根据sys.path
# sys.path.insert()

# from imp import reload (重新加载)
# reload(aa)

# 如果是模块引入,都是开辟的新的内存空间 

# __dict__ 获取所有属性
class Test(object):
  def __init__(self,name):
    self.__name = name
a = Test('laowang')
# a.__dict__

""" 魔法方法 """
# 1. __dict__ 检测类或对象中的所有方法
# 2. __init__ 初始化方法
# 3. __del__ 删除方法 
# 4. __call__ 对象直接调用,会调call
# 5. __str__ 获取对象的描述
# 6. __doc__ 获取对象的描述
# 7. __module__ __class__,
# 8. __getslice__, __setslice__, __delslice__ 用于分片操作, 切片的获取,切片设置,切片删除
# 9. __getitem__, __setitem__, __delitem__ 用于索引操作 ,对象属性获取,对象属性的设置,对象属性删除