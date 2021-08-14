def max(x, y):
    if x > y:
        min = y
    else:
        min = x

    for i in range(1, min+1):
        if((x % i == 0) and (y % i ==0)):
            max = i

    return max
num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))
print(num1, "和", num2,"的最大公约数为：", max(num1, num2))
'''
return语句的作用，返回第一个值，并且不会再返回。
'''