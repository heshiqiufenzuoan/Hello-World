'''
捕获已知错误
'''
try:
    num = int(input("请输入一个整数:"))
    result = 8 / num
    print(result)
except ZeroDivisionError:
    print("整数不能为0，请从新输入")
except ValueError:
    print("您输入的为字母，不是整数，请从新输入")
