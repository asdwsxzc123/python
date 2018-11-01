a = []
# i = 10
# while i<=77:
#   a.append(i)
#   i += 1

# for i in range(10,78):
#   a.append(i)

# print(range(10,78))

# range python2太大会溢出,python3不会,要的时候在生成给出,占得内存小
# 列表生成
# a = [i for i in range(1,18)]

# a = [11 for i in range(1,18)]

# a = [i for i in range(1,20) if i%2 ==0]

# a = [i for i in range(3) for j in range(2)]

a = [(i,j) for i in range(3) for j in range(2)]

print(a)

