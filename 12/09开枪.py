class Person(object):
    def __init__(self, name):
        super(Person, self).__init__()
        self.name = name  # 人的名称
        self.gun = None
        self.hp = 100
    def anzhuang_zidan(self, dan_jia_temp, zi_dan_temp):
        # 弹夹.保存子弹(子弹)
        dan_jia_temp.baocun_zidan(zi_dan_temp)
    
    def anzhuang_danjai(self, gun_temp, dan_jia_temp):
        # 弹夹.保存子弹(子弹)
        gun_temp.baocun_danjia(dan_jia_temp)
    def naqiang(self, gun_temp):
        """ 老王拿枪 """
        self.gun = gun_temp
    def __str__(self):
        if (self.gun):
            return '%s的血量为:%d,他有枪,%s'%(self.name, self.hp,self.gun)
        else:
            if self.hp > 0:
                return '%s的血量为:%d,他没有枪'%(self.name, self.hp)
            else:
                return '%s死了'%(self.name)
    def koubanji(self,diren):
        """ 让枪发射子弹去打敌人 """
        # 枪开火(diren)
        self.gun.fire(diren)
    def diaoxue(self,zidan_weili):
        """ 子弹让敌人掉血 """
        # 枪开火(zidan_weili)
        self.hp -= zidan_weili
        

class Gun(object):
    def __init__(self, name):
        super(Gun, self).__init__()
        self.name = name  # 枪的名称
        self.danjia = None #用来记录弹夹对象的引用
    def __str__(self):
        if self.danjia:
            return '枪的信息为:%s,弹夹为:%s'%(self.name,self.danjia)
        else:
            return '枪的信息为:%s,这把枪没有弹夹'%(self.name)
    def baocun_danjia(self, dan_jia_temp):
        # 枪保存弹夹
        self.danjia = dan_jia_temp
    def fire(self, diren):
        # 枪打敌人,子弹打的,弹夹拿子弹
        # 弹夹去子弹,需要返回子弹
        zidan_temp = self.danjia.tanchu_zidan()
        # 子弹打敌人
        if zidan_temp:
            zidan_temp.dazhong(diren)
        else:
            print('弹夹中没有子弹了')

class Danjia(object):
    def __init__(self, max_num):
        super(Danjia, self).__init__()
        self.max_num = max_num  # 用来记录最大弹夹数
        self.zidan_list = []  # 记录所有的子弹的引用
    def __str__(self):
        return '弹夹的信息为:%d/%d'%(len(self.zidan_list), self.max_num)
    def baocun_zidan(self, zi_dan_temp):
        # 保存子弹
        self.zidan_list.append(zi_dan_temp)
    def tanchu_zidan(self):
        # 弹出子弹
        if self.zidan_list:
            return self.zidan_list.pop()
        else:
            return None


class Zidan(object):
    def __init__(self, sha_shang_li):
        super(Zidan, self).__init__()
        self.sha_shang_li = sha_shang_li  # 子弹的威力
    def dazhong(self, diren):
        """ 子弹打中敌人 """
        diren.diaoxue(self.sha_shang_li)

def main():
    # 1 创建一个人
    laowang = Person('老王')

    # 2 创建一个枪
    ak47 = Gun('AK45')

    # 3 创建一个弹夹
    dan_jia = Danjia(20)

    # 4 创建一些子弹
    for i in range(15):
        zi_dan = Zidan(10)

        # 5 老王吧子弹安装到弹夹中(弹夹,子弹)
        laowang.anzhuang_zidan(dan_jia, zi_dan)

    # 6 老王吧弹夹安装到枪中(枪,弹夹)
    laowang.anzhuang_danjai(ak47, dan_jia)

    # 测试弹夹
    # print(ak47)
    # print(dan_jia)

    # 7 老王拿枪
    laowang.naqiang(ak47)
    print(laowang)

    # 8 创建一个敌人
    gebi_laosong = Person('隔壁老宋')

    # 9 老王开枪打敌人
    for i in range(10):
        laowang.koubanji(gebi_laosong)
        print(laowang)
        print(gebi_laosong)

if __name__ == '__main__':
    main()
