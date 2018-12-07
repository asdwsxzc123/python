# restful风格
# 一般解释为'表现层状态转换'


特点:
1.具象的,表现的对象就是资源
2. 表现: 资源的表现形式, Accept和content-type 
3.状态转换: 客户端和服务端交互的过程
# HTTP请求
# GET 查询
# POST 保存
# PUT 修改
# DELETE 删除
restful架构
每个URL表示一种资源
客户端与服务端,传递这种资源的某种表现层
客户端通过四个http动词,对服务器资源进行操作,实现表现层转换

""" 操作 """
# 获取
get goods/ID
# 创建
POST goods
# 更新
PUT goods/id
# 删除
DELETE goods/ID

""" 查询条件 """
# 返回数据的指定数量
goods?limit=10
# 返回指定数据的开始位置
goods?offset=10
# 指定第几页,以及每页数据的数量
goods?page=2&per_page=20

""" 状态码 """
200 OK 服务器成功返回的状态码
201 CREATED: 用户新建或修改数据
202 accepted: 请求进入后台
400 invalid request: 用户发送的请求有错误
401 unauthorized: 用户没有权限
403 forbidden: 访问被禁止
404 notfoun 请求针对的不存在
406 not acceptable: 用户请求的格式不正确
500 internal server error 服务器发生错误