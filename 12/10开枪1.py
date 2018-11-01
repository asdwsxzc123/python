class Person(object):
    def __init__(self,name):
        self.name = name
        self.gun = None
        self.hp = 100
    def __str__(self):
        if (self.gun):
            return '%s的血量为:%d,他有枪:%s '%(self.name,self.hp,self.gun)
        else :
            if (self.hp > 0):
                return '%s的血量为:%d,他没有枪'%(self.name,self.hp)
            else :
                return '%s死了'%(self.name)

    def na_qiang(self,gun_temp):
        self.gun = gun_temp
    def anzhuang_zidan(self,dan_jia_temp,zi_dan_temp):
        dan_jia_temp.baocun_zidan(zi_dan_temp)
    def anzhuang_danjia(self,dan_jia_temp,gun_temp):
        gun_temp.baocun_danjia(dan_jia_temp)
    def fire(self,diren):
        self.gun.fachu_zidan(diren)
    def diaoxue(self,zidan_weili):
        self.hp -= zidan_weili
        


class Gun(object):
    def __init__(self,name):
        self.name = name
        self.danjia = None
    def __str__(self):
        return '枪的信息:%s,弹夹信息:%s'%(self.name,self.danjia)
    def baocun_danjia(self, danjia_temp):
        self.danjia = danjia_temp
    def fachu_zidan(self, diren):
        zidan_temp = self.danjia.tanchu_zidan()
        if zidan_temp:
            zidan_temp.jizhong_diren(diren)
        else: 
            print('没有子弹了')

class Dan_jia(object):
    def __init__(self,max_num):
        # 弹夹最大容量
        self.max_num = max_num
        self.zidan_list = []
    def __str__(self):
        return '弹夹信息:%d/%d'%(len(self.zidan_list), self.max_num)
    def baocun_zidan(self,zi_dan_temp):
        if len(self.zidan_list) <20:
            self.zidan_list.append(zi_dan_temp)
        else :
            print('上满子弹了')
    def tanchu_zidan(self):
        if (self.zidan_list):
            return self.zidan_list.pop()
        else : None

class Zi_dan(object):
    def __init__(self,zidan_weili):
        # 弹夹威力
        self.zidan_weili = zidan_weili
    def __str__(self):
        return '子弹威力:%d'%(self.zidan_weili)
    def jizhong_diren(self,diren):
        diren.diaoxue(self.zidan_weili)
            
        

def main():
    # 老王开枪

    # 1.创建老王
    laowang = Person('老王')
    # 2. 创建枪
    ak47 = Gun('AK47')
    # 3. 创建弹夹
    dan_jia = Dan_jia(20)
    for i in range(21):
        # 4. 创建子弹
        zi_dan = Zi_dan(10)
        # 5. 老王吧子弹装进弹夹
        laowang.anzhuang_zidan(dan_jia,zi_dan)
    # 6. 弹夹装进枪
    laowang.anzhuang_danjia(dan_jia,ak47)
    # 7. 老王拿枪
    laowang.na_qiang(ak47)
    # 8. 创建敌人
    gebi_laosong = Person('隔壁老宋')
    print(laowang)
    print(gebi_laosong)
    # 9. 老王开枪
    for i in range(20):
        laowang.fire(gebi_laosong)
        # 10. 枪射击敌人
        print(gebi_laosong)
        if (gebi_laosong.hp <= 0):
            break
    # 11. 敌人中弹

if(__name__ == '__main__'):
    main()
    
    