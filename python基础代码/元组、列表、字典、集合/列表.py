'''
标准数据类型 包括可变数据类型和不可变数据类型：
    不可变数据类型：数字number、字符串string、元组tuple
    可变数据类型：列表list、字典dictioary、集合set
'''

# 创建列表
list = [1, 2, 3, 4, 5]
print(list)
'''
把列表当作堆栈(后进先出)使用：
    1.用append（）方法可以把一个元素添加到堆栈顶。
    2.用不指定索引的pop（）方法可把一个元素从堆栈中释放出来。
'''
# list.append(x)：append--附加，把一个元素添加到列表的结尾。
list_stack = [1, 2, 3, 4, 5]
list_stack.append(6)  #append()只需要一个argument参数
list_stack.append('dfg')
list_stack.append(8)
list_stack.pop()  #把最后一个元素8释放出来
list_stack.pop()  #此时已经倒数第二个dfg元素释放出来
print(list_stack)
print('----------------------')
'''
把列表当作队列使用：
补：队列：先进先出
1.缺点：总体效率不高，列表子啊开始插入和弹出的速度不快。
2.有点：列表最后添加或弹出的速度快。
'''
from collections import deque
list_queue = deque(['q', 'w', 'e', 'r', 't']) #将队列里面第一个元素取出来
list_queue.append(3)
list_queue.popleft()
print(list_queue)
print('----------------------')

'''
列表推导式：提供了从序列创建列表的简单途径。
    1.每个推导式都在for之后跟一个表达式，然后有0到多个for或if语句
    2.返回结果是一个根据表达式其后的for和if根据上下文环境生成的列表 
'''
vec = [1, 2, 3, 4, 5]
a = [3*x for x in vec]
print(a)
print('-----------------------')
'''
嵌套列表解析
'''
# 3 x 4的矩阵列表
matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15]
]
print(matrix)

#将3 x 4的矩阵换成4 x 3的矩阵，即矩阵转置
matrix_transpose = []
for i in range(5):
    matrix_transpose.append([row[i] for row in matrix])
print(matrix_transpose)
print("----------------------------")

'''
删除del
'''
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print(a)
b = [-1, 1, 66.25, 333, 333, 1234.5]
del b[3:]
print(b)
print("---------------------------")

'''
遍历技巧
'''
# 在字典中遍历
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# 在序列中遍历时，所应位置和对应的值可以使用enumerate（）函数
enumerate1 = ['tic', 'tac', 'toe']
for i in enumerate(enumerate1):
    print(i, v)

#同时遍历两个或更多个序列
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
    '''
        >>>"{} {}".format("hello", "world")    # 不设置指定位置，按默认顺序
        'hello world'
 
        >>> "{0} {1}".format("hello", "world")  # 设置指定位置
        'hello world'
 
        >>> "{1} {0} {1}".format("hello", "world")  # 设置指定位置
        'world hello world'
    '''
print('-----------------------------------')
