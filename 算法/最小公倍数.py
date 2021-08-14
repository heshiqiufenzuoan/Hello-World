def multipel(x, y):

    if x > y:
        bigger = x
    else:
        bigger = y

    while(True):
        if((bigger % x == 0) and (bigger % y ==0)):
            multipel = bigger
            break
        else:
            bigger += 1
    return multipel


num1 = int(input("输入第一个数字: "))
num2 = int(input("输入第二个数字: "))

print(num1, "和", num2, "的最小公倍数为", multipel(num1, num2))

