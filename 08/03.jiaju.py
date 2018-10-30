class Home:
    def __init__(self, new_area, new_info, new_addr):
        self.area = new_area
        self.info = new_info
        self.addr = new_addr
        self.left_area = new_area
        self.contain_items = []

    def __str__(self):
        msg = '房子的面积是:%d,户型是:%s,地址是:%s,剩余面积:%s' % (self.area, self.info, self.addr, self.left_area)
        
        msg += ' 当前房子里的物品有%s'%(str(self.contain_items))
        return msg

    def add_item(self, item):
        # 直接定义
        self.left_area = self.left_area - item.area
        self.contain_items.append(item.name)
        # 通过方法获取
        self.left_area = self.left_area - item.get_area()
        self.contain_items.append(item.get_name())

class Bed:
    def __init__(self, new_name, new_area):
        self.name = new_name
        self.area = new_area

    def __str__(self):
        return '床的品牌:%s,占用的面积%d平米' % (self.name, self.area)

    def get_area(self):
      return self.area
    def get_name(self):
      return self.name

fangzi = Home(126, '三室一厅', '北京市 朝阳区 长安街 666号')
print(fangzi)

bed1 = Bed('席梦思', 4)
bed2 = Bed('双人床', 4)
fangzi.add_item(bed1)
fangzi.add_item(bed2)
print(fangzi)
