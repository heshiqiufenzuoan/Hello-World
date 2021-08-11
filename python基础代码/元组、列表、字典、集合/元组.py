'''
元组不能进行增删改
'''
'''
标准数据类型：（包括可变数据类型，不可变数据类型）
    1.可变数据类型：列表list、字典dictiongary、集合set。
    2.不可变数据类型：数字number、字符串string、元组tuple。
'''
# 创建元组
tuple = (1, 2, 3, 4, 5)
tuple2 = (6, 7, 8, 9, 0)
print("tuple元组中的元素为：", tuple)
print("tuple2元组中的元素为：", tuple2)
print("-----------------------------------")
# 访问元组
print("tuple[0]：", tuple[0])  # tuple1元组中第一个元素
print("tuple2[2]：", tuple2[2])  # tuple2元组中第三个元素
print("------------------------------------")
# 修改元组
tuple = (1, 2, 3, 4, 5, 6)
print("修改后的tuple1元组为：", tuple)
print("------------------------------------")
# 删除元组
'''
    因为元组为不可变数据类型，所以不能删除，只要删除就会报错。
'''
# 元组运算符
# 1.计算元组个数
num = len(tuple2)
print("tuple2元组元素个数为：", num)
# 2.连接元组
tuple3 = tuple2 + tuple  # tuple1 + tuple2 与 tuple2 + tuple1
print("新组成的tuple3元组中元素为：", tuple3)
# 3.复制元组
tuple4 = ('Hi') * 4
print("tuple4元组的元素为：", tuple4)
# 4.查看元素是否存在
judge = 3 in (1, 2, 3) #judge判断的意思
print(judge)
print("-------------------------------------")
# 5.迭代
# 方法一：
for i in tuple:
    print(i, end=' ')
# 方法二：
it = iter(tuple4)
print(next(it))
'''
注意：tuple中没有‘__next__'属性，不能使用'__next__'，
否则会报如下错误：AttributeError: 'tuple' object has no attribute '__next__'
例:
a = ('csd', 'dwe', 'DWE')
it = iter(a)
print(a.__next__())
'''
# 6.元组的索引、截取
a = tuple4[2]
print('第三个元素：', a)
print('tuple3元组第三个元素', tuple3[2])
# 7. 元组内置函数
a = len(tuple3)  # tuple3元组长度
print('tuple3元组长度:', a)

max = max(tuple3) # tuple3元组中最大元素值
print('最大元素值:', max)

min = min(tuple3) # tuple3元组中最小元素值
print('最小元素值:', min)











