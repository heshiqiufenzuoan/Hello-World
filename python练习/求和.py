'''
实现求和的几种方法
'''

# 第一种
l = range(1, 101)
print(sum(l))

# 第二种
print(sum(range(1, 101)))

#第三种
sum = 0
for i in range(0, 100):
    sum += (i+1)
print(sum)

#第四种
i = sum = 0
while i < 100:
    i += 1
    sum = sum + i
print(sum)


