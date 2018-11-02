class SweetPotato:
    def __init__(self):
        self.cookedString = '生的'
        # 0-3生,3-5半生,5-8熟的,
        self.cookedLevel = 0
        self.condiments = []
    def __str__(self):
        return ('地瓜的状态:%s(%d),添加的作料有%s' % (self.cookedString, self.cookedLevel, str(self.condiments)))

    def cook(self, cooked_time):
        self.cookedLevel += cooked_time
        if self.cookedLevel > 8:
            self.cookedString = '烤糊了'
        elif self.cookedLevel >= 5:
            self.cookedString = '烤熟了'
        elif self.cookedLevel >= 3:
            self.cookedString = '半生了'
        else:
            self.cookedString = '生的'

    def addCondiments(self, item):
      self.condiments.append(item)

di_gua = SweetPotato()
while True:
    time = int(input('请输入烤的时间:'))
    if time > 20:
        break
    di_gua.cook(time)
    di_gua.addCondiments('番茄酱')
    print(di_gua)
