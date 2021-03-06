list的下标就是偏移量的意思
list的数据在内存中的位置
# li[3] = 0X23 + 3*4Byte
1. 普通顺序表
直接存储元素
2. 元素外置顺序表
存储的是元素索引,在去找元素

# 顺序表的结构
1.需要表头信息, 容量和个数
2. 数据区: 存入的数据
一个顺序表完整信息,一是元素集合,二是为实现正确操作而需记录的信息.元素存储区的容量和当前表中已有的元素个数

# 顺序表的两种实现方式
1. 一体式结构: max,num,元素存储区连续存储
2. 分离式结构: max,num,指向元素存储区分离

元素存储区替换
一体式结构:由于顺序表信息去与数据区连续存储在一起,所以若想更换数据区,测只能整体搬迁,既整个顺序表对象改变了
分离式结构: 只需要跟换链接级地址

元素存储区扩充:
分离式知悉要对存储区域进行扩充,使用这个表的地方都不必修改,动态顺序表,容量在使用中动态变化
策略
1. 每次扩充增加固定数目的存储位置,每次扩充增加10个元素,线性增长
 特定: 节约空间,扩充平凡,操作次数多
 2. 每次扩充容量加倍,每次扩充增加一倍空间 
 特定: 减少了扩充操作的执行次数, 但可能会浪费空间资源, 以用空间换时间
