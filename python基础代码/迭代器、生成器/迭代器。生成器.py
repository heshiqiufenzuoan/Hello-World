list = [1, 2, 3, 4, 5]
it = iter(list)
print(next(it)) #生成1
print(next(it)) #生成2
print(next(it)) #生成3
print(next(it)) #生成4
print(it.__next__()) #生成5
# for i in it:
#     print('\n',i, end=" ")

print("=====================")
l = [1, 2, 3, 4, 5]
l_iter = l.__iter__() #创建一个迭代器
while True:
    try:
        item = l_iter.__next__()
        print(item, end=" ")
    except StopIteration:
        break

'''======================================='''

# 生成器
'''
本质就是一个迭代器
1. 生成器函数
2. 生成器表达式
'''
def produce():
    for i in range(200):
        yield "做的第%s碗面条"%(i+1)
g = produce()
print(g)  # g代表的是generation
print(g.__next__())
print(g.__next__())
print(g.__next__())

#列表推导式
a = ['学生%s'%i for i in range(10)]
print(a)

#生成器表达式
b = ('学生%s'%i for i in range(10))
print(b)  #得到一个生成器对象
print(b.__next__())
print(next(b))      #与print(b.__next__())生成方法一样。
print(b.__next__())
print(b.__next__())
print(b.__next__())


























