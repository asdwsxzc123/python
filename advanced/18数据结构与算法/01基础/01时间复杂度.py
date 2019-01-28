# 时间复杂度O
# 每台机器执行的总时间不同,但执行基本运算数量大体相同

# 抽象数据类型(ADT)
 
# 算法
算法就是将思路用程序表达出来,算法是独立存在的一种解决问题的方法和思路

五大特性
1. 输入: 算法具有0个或多个输入
2. 输出: 算法至少有一个或多个输出
3. 有穷性: 在有限的步骤之后自动结束,而不会无限循环,每一个步骤可以在接受的时间内完成
4. 确定性: 每一步都有确定的含义,不会出现二义性
5. 可行性: 每一步都是可行的,每一步能够给执行有限的次数完成

# 最坏时间复杂度
算法完成的工作最少需要多少基本操作: 最优时间复杂度
算法完成的工作最多需要多少基本操作: 最坏时间复杂度
算法完成的工作平均需要多少基本操作: 平均时间复杂度

# 基本计算规则
1. 基本操作,时间复杂度O(1)
2. 顺序结构,时间复杂度按加法计算
3. 循环结构, 时间复杂度按乘法计算
4. 分支结构, 时间复杂度取最大值
5. 判断一个算法的效率,只需要关注操作次数的最高次项,其他可以忽略
6. 在没有特殊说明,分析时间复杂度按最坏时间复杂度

常见的时间复杂度
12 O(1) 常数阶
2n+3 O(n) 线性阶
3n^2+2n+1 O(n^2) 平方阶
5log2n + 20 O(logn) 对数阶
# 以2位低
2n+3nlog2n+19 O(nlogn) nlogn阶
6n^3 + 2n^2 +3n + 4 O(n^3) 立方阶
2^n O(2^n) 指数阶

O(1) < O(logn) <  O(n) < O(nlogn) < O(2^n) < O(n^2) <  O(n^3)


""" list内置方法时间效率 """
# extend: 1.9s
# append: 2s
# insert: 30s
# +: 1.5s
# [i for i in range]: 0.6s
# list(range()): 0.4s
index O(1)
append O(1)
pop O(1)
pop(i) O(n),最坏情况第一个
insert(i, item) O(n)
del operator 需要一个一个清空,
iteratain O(n)
contains(in) O(n)
get slice[x:y] O(k)
del slice O(n)
set slice O(n + k)
reverse O(n)
concatenate O(k)
sort O(n log n)
multiply O(nk)

""" 字典 """
copy O(n)
get item O(1)
set item O(1)
delete item O(1)
contains(in)  O(1)
iteration  O(n)