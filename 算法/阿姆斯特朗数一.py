num = int(input("请输入一个数字: "))
sum = 0
'''
如果没有这一行，那么将会出现以下错误：
TypeError: unsupported operand type(s) for +=: 'builtin_function_or_method' and 'int'
'''
n = len(str(num))
replace = num
while replace > 0:
    op = num % 10
    sum += op ** n
    replace = replace // 10

if sum == num:
    print(num, "是阿姆斯特朗数")
else:
    print(num, "不是阿姆斯特朗数")
