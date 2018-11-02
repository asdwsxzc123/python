# import sendmsg
# sendmsg.test1()


from sendmsg import test1,test2
test1()
test2()

# 尽量不要使用*,如果有两个模块,都有同一个方法,会导致后面的顶替前面的
from sendmsg import *
test1()
# __name__如果自执行:交__main__,如果是引入的模块,叫模块名
print(__name__)
# import sendmsg as 