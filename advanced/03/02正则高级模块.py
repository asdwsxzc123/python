import re
""" search """
# 只能取到第一个
# ret = re.search(r'\d+', '阅读数为 9999')
# print(ret.group())

""" findall """
# 统计出 python，c,c+阅读次数,分组
# ret = re.findall(r'\d+', 'python = 999,c =822, c++ = 232')
# print(ret)

""" sub """
#  将匹配到的数据进行替换,替换在返回值里面
# 方法一
# ss = 'python = 997'
# ret = re.sub(r'\d+', '998', ss)
# print(ss)
# print(ret)

# 方法2
# def add(temp):
#   strNum = temp.group()
#   num = int(strNum) + 1
#   return str(num)
# ret = re.sub(r'\d+', add, 'python =996')
# print(ret)

""" split """
# ret = re.split(r':| ', 'info:dsfsdf 33 shangdong')
# print(ret)


html_st = """ 
<dd class="job_bt">
        <h3 class="description">职位描述：</h3>
        <div>
        <p>工作内容：</p>
<p>参与糗事百科的后端研发；</p>
<p>保障产品的快速迭代与服务质量；</p>
<p>任职资格：</p>
<p>三年以上高并发系统的设计与调优经验，对系统的架构与实现有清晰的认识；</p>
<p>熟悉linux系统生产环境搭建与调优；</p>
<p>至少熟悉 Python/Golang/C/C++ 其中一种语言</p>
<p>熟练掌握Mysql数据库的使用与优化；</p>
<p>熟悉至少一种web框架的使用和调优，并了解其基本原理</p>
<p>扎实的编程功底，能享受编程乐趣；</p>
<p>高效的学习能力和分析解决问题能力；</p>
<p>本科及以上学历；</p>
<p><br></p>
<p>加分项：有团队管理经验，团队驱动力者优先~ ~</p>
        </div>
    </dd> """

ret = re.sub(r'</?\s?\w*>', '', html_st)
# ret = re.sub(r'</?\s?\w*>', '', html_st)
print(ret)