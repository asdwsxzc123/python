class Person(object):
    def __init__(self, name):
        super(Person, self).__init__()
        self.name = name  # 人的名称

    def anzhuang_zidan(self, dan_jia_temp, zi_dan_temp):
        # 弹夹.保存子弹(子弹)
        dan_jia_temp.baocun_zidan(zi_dan_temp)
    
    def anzhuang_danjai(self, gun_temp, dan_jia_temp):
        # 弹夹.保存子弹(子弹)
        gun_temp.baocun_danjia(dan_jia_temp)


class Gun(object):
    def __init__(self, name):
        super(Gun, self).__init__()
        self.name = name  # 枪的名称
        self.danjia = None #用来记录弹夹对象的引用
    def baocun_danjia(self, dan_jia_temp):
        # 枪保存弹夹
        self.danjia = dan_jia_temp

class Danjia(object):
    def __init__(self, max_num):
        super(Danjia, self).__init__()
        self.max_num = max_num  # 用来记录最大弹夹数
        self.zidan_list = []  # 记录所有的子弹的引用

    def baocun_zidan(self, zi_dan_temp):
        # 保存子弹
        self.zidan_list.append(zi_dan_temp)


class Zidan(object):
    def __init__(self, sha_shang_li):
        super(Zidan, self).__init__()
        self.sha_shang_li = sha_shang_li  # 子弹的威力


def main():
    # 1 创建一个人
    laowang = Person('老王')

    # 2 创建一个枪
    ak47 = Gun('AK45')

    # 3 创建一个弹夹
    dan_jia = Danjia(20)

    # 4 创建一些子弹
    zi_dan = Zidan(10)

    # 5 老王吧子弹安装到弹夹中(弹夹,子弹)
    laowang.anzhuang_zidan(dan_jia, zi_dan)
    # 6 老王吧弹夹安装到枪中(枪,弹夹)
    laowang.anzhuang_danjai(ak47, dan_jia)
    # 7 老王拿枪

    # 8 创建一个敌人

    # 9 老王开枪打敌人


if __name__ == '__main__':
    main()
