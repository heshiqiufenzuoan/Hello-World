'''
捕获已知错误
'''
try:
    num = int(input("请输入一个整数:"))
    result = 8 / num
    print(result)

except ValueError:
    print("您输入的为字母，不是整数，请从新输入")
except Exception as result:
    print("未知错误：%s" % result)
else:
    print("尝试成功")
finally:
    print("finally下方代码无论是否输入成功都会执行的代码")
print("--" * 50)