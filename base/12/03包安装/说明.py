"""
1 .包同级创建 setup.py

2.内容
from distutils.core import setup

setup(name="li", version="1.0", description="module",
      author="li", py_modules=["testMsg.sendMsg","testMsg.recvmsg"])

3. cmd输入命令 python setup.py build 构建出build/lib

4.python setup.py sdist  打包成了tar.gz

5. 解压
  cp dist/li-1.0.tar.gz 
  tar -zxvf 
  python setup.py install
  sudu 权限
"""