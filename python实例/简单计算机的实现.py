'''
此计算机仅限两个数的加减乘除
'''
# 定义加的函数
def add(x, y):
    return x + y

# 定义减的函数
def reduce(x, y):
    return x - y

# 定义乘的函数
def take(x, y):
    return  x * y

# 定义除的函数
def remove(x, y):
    return x / y

print("加减乘除分别为1，2，3，4。")
choice = str(input("请选择运算："))
num1 = float(input("请输入第一个数："))
num2 = float(input("请输入第二个数："))

if choice == '1':
    print(num1, "和", num2, "相加结果为：", add(num1, num2))
elif choice == '2':
    print(num1, "和", num2, "相减结果为：", reduce(num1, num2))
elif choice == '3':
    print(num1, "和", num2, "相乘结果为：", take(num1, num2))
elif choice == '4':
    print(num1, "和", num2, "相加结果为：", remove(num1, num2) )
else:
    print("您输入的格式不正确！！！")