# orm: object relational mapping 对象-关系映射
# 创建一个实例对象,用创建他的类名当做数据表名,用创建他的类属性对应数据表的字段,当对这个实例对象操作时,能够对应mysql语句

# 类名对应表,属性名对应字段


# class User():
#     uid = ('uid', 'int unsigned')
#     name = ('username', 'varchar(30)')
#     email = ('email', 'varchar(30)')


# u = User(uid=123, name='laowang', email='xxx@126.com', password='123456')
# u.save()
# insert into User (uid, name,email) values (123,'laowang', 'xxx@126.com')


class ModelMateClass(type):
    def __new__(self, name, bases, attrs):
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v, tuple):
                print('found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        # 删除这些在字点中存储的属性
        for k in mappings.keys():
            attrs.pop(k)

        # 将之前的ui等及对应的对象引用
        attrs['__mappings__'] = mappings
        attrs['__table__'] = name
        return type.__new__(cls, name, bases, attrs)


class User(metaclass=ModelMateClass):
    uid = ('uid', 'int unsigned')
    name = ('username', 'varchar(30)')
    email = ('email', 'varchar(30)')
    def __init__(self, **kwargs):
      for name, value in kwargs.items():
        setattr(self, name,value)
        # self.name = value
    def save(self):
      fields = []
      args = []
      for k, v in self.mappings__.items():
        fields.append(v[0])
        args.append(getattr(self,k,None))
      # sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(field), ','.join([str(i) for i in args ]))
      args_temp = list()
      for temp in args:
        if isinstance(temp, int):
          args_temp.append(str(temp))
        elif isinstance(temp, str):
          args_temp.append("'%s'" % temp)
      sql = 'insert into %s (%s) values (%s)' % (
          self.__table__, ','.join(field), ','.join(args_temp))
      print('SQL: %s' % sql)

u = User(uid=123,name='123d',email="sdfsdf@126.com")
u.save()
