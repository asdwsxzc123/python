# pip install redis
# pip install django-redis-sessions == 0.5.6

from redis import StrictRedis

if __name__ == "__main__":
    # 创建一个redis对象
    try:
      sr = StrictRedis(password=123456)
      # 添加一个值
      # sr = StrictRedis(host='193.168.220.137', port=6379, db=0)
      # res = sr.set('name', 'lisi')
      # res = sr.get('name')

      # 删除name及对应的值
      # res = sr.delete('name')

      # 删除多个键值
      # res = sr.delete('name', 'a2')

      # 获取数据库中所有的列表
      res = sr.keys()
      print(res)

    except Exception as e:
      print(e)


# 集群
if __name__ == "__main__":
    # 创建一个redis对象
    try:
      startup_nodes = [
        {
          'host': '172.16.179.131', 'port' : '7000'
        }
      ]
      src = StrictRedisCluster(startup_nodes= startup_nodes, decode_respose=True)
      result = src.set('name', 'lisi')

    except Exception as e:
      print(e)
