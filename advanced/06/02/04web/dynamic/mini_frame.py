import re
from pymysql import connect
import urllib

""" 
URL_FUNC_DICT = {
    "/index.html": index,
    "/center.html": center,
} """
URL_FUNC_DICT = dict()
def route(url):
    def set_func(func):
        URL_FUNC_DICT[url] = func
        def call_func(*args,**kwargs):
            return func(*args,**kwargs)
        return call_func
    return set_func
def select_list(sql):
    conn = connect(host='172.16.20.46', port=3306, user='root', password='123456', database='stock_db', charset='utf8')
    # 获取cursor对象
    cursor = conn.cursor()
    row = cursor.execute(sql)
    stock_info = cursor.fetchall()
    cursor.close()
    conn.close()
    return row, stock_info
def execute_mysql(sql):
    conn = connect(host='172.16.20.46', port=3306, user='root', password='123456', database='stock_db', charset='utf8')
    # 获取cursor对象
    cursor = conn.cursor()
    row = cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
    return row
@route(r'/index.html')
def index(ret):
    with open('./templates/index.html') as f:
        content = f.read()

    # my_stock_info = '哈哈 这是你本月的名称'
    # content = re.sub(r'\{%content%\}', my_stock_info, content)
    (row, stock_info) = select_list('select * from info;')
    tr_template = """<tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>
            <input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="%s">
        </td>
        </tr>
    """
    html = ''
    for line_info in stock_info:
        html += tr_template % (line_info[0],line_info[1],line_info[2],line_info[3],line_info[4],line_info[5],line_info[6],line_info[7],line_info[1])
    content = re.sub(r'\{%content%\}', html, content)
    return content

@route(r'/center.html')
def center (ret):
    with open('./templates/center.html') as f:
        content = f.read()
    # my_stock_info = '这里是从mysql查询出来的数据...'
    # content = re.sub(r'\{%content%\}', my_stock_info, content)
    (row, stock_info) = select_list("select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info as i inner join focus as f on i.id=f.info_id;")
    
    tr_template = """
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>
                <a type="button" class="btn btn-default btn-xs" href="/update/%s.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a>
            </td>
            <td>
                <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="%s">
            </td>
        </tr>
    """
    html = ''
    for line_info in stock_info:
        html += tr_template % (line_info[0],line_info[1],line_info[2],line_info[3],line_info[4],line_info[5],line_info[6],line_info[0],line_info[0])
    content = re.sub(r'\{%content%\}', html, content)
    return content

@route(r'/update/(\d+)\.html')
def show_update_page (ret):
    with open('./templates/update.html') as f:
        content = f.read()
    stock_code = ret.group(1)
    (row, stock_info) = select_list("SELECT note_info FROM focus WHERE info_id= (SELECT id FROM info WHERE CODE=%s);"%stock_code)

    for line_info in stock_info:
        html = line_info[0]
    content = re.sub(r'\{%code%\}', stock_code, content)
    content = re.sub(r'\{%note_info%\}', html, content)
    return content



# 添加正则拍匹配带参数的
@route(r'/add/(\d+)\.html')
def add_focue(ret):
    # 1. 获取股票代码
    sotck_code = ret.group(1)
    # 2. 判断试下是否有这个股票代码
    (row, stock_info) = select_list('SELECT * FROM info WHERE CODE=%s;'%sotck_code)
    if (row==0):
        return '不存在该股票代码'
    
    # 3. 判断一下是否已经关注过
    (row1, stock_info1) = select_list('SELECT * FROM info AS i INNER JOIN focus AS f ON i.id = f.`info_id` WHERE i.code=%s;'%sotck_code)
    if (row1 == 0):
        execute_mysql('INSERT INTO focus (info_id)  SELECT id FROM info AS i WHERE i.code=%s;'%sotck_code)
        return 'add %s ok...' % sotck_code
    else: 
        return '已存在股票代码:%s' % sotck_code
@route(r'/del/(\d+)\.html')
def del_focue(ret):
    # 1. 获取股票代码
    sotck_code = ret.group(1)
    print(sotck_code)
    # 2. 判断试下是否有这个股票代码
    (row, stock_info) = select_list('SELECT * FROM info WHERE CODE=%s;'%sotck_code)
    if (row==0):
        return '不存在该股票代码'
    
    # 3. 判断一下是否已经关注过
    print('SELECT * FROM focus where info_id= select id from info WHERE CODE=%s;'%sotck_code)
    (row1, stock_info1) = select_list('SELECT * FROM focus where info_id= (select id from info WHERE CODE=%s);'%sotck_code)
    if (row1 > 0):
        execute_mysql('DELETE FROM focus WHERE info_id =(SELECT i.id FROM info AS i WHERE i.code=%s);'%sotck_code)
        return '已取消关注,股票代码为 %s ok...' % sotck_code
    else: 
        return '未关注该股票代码:%s' % sotck_code
@route(r'/update/(\d+)/(\w+)\.html')
def update_focue(ret):
    # 1. 获取股票代码
    sotck_code = ret.group(1)
    remark = ret.group(2)
    remark = urllib.parse.unquote(remark)
    print(remark)
    # 2. 判断试下是否有这个股票代码
    (row, stock_info) = select_list('SELECT * FROM info WHERE CODE=%s;'%sotck_code)
    if (row==0):
        return '不存在该股票代码'
    
    # 3. 判断一下是否已经关注过
    print('SELECT * FROM focus where info_id= select id from info WHERE CODE=%s;'%sotck_code)
    (row1, stock_info1) = select_list('SELECT * FROM focus where info_id= (select id from info WHERE CODE=%s);'%sotck_code)
    if (row1 > 0):
        execute_mysql('UPDATE focus SET note_info=%s WHERE info_id= (SELECT id FROM info WHERE CODE=%s);'%(remark,sotck_code))
        return '更新成功,股票代码为 %s ok...' % sotck_code
    else: 
        return '未关注该股票代码:%s' % sotck_code
def application(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html;charset=utf-8')])
    
    file_name = env['PATH_INFO']
    # file_name = "/index.py"

    
    # if file_name == "/index.py":
    #     return index()
    # elif file_name == "/center.py":
    #     return center()
    # else:
    #     return 'Hello World! 我爱你中国....'
   

    try:
        # func = URL_FUNC_DICT[file_name]
        # return func()
        # return URL_FUNC_DICT[file_name]()
        # 返回以对象形式,url是key, func是值
        for url, func in URL_FUNC_DICT.items():
            # {
            #   r"/index.html":index,
            #   r"/center.html":center,
            #   r"/add/\d+\.html":add_focus
            # }
            ret = re.match(url, file_name)
            if ret:
                return func(ret)
        else: 
            return '请求的url(%s)没有对应的函数...'%file_name

    except Exception as ret:
        return "产生了异常：%s" % str(ret)






