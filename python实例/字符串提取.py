# 判断用户输入的是否为阿姆斯特朗数
num = int(input("请输入一个正整数："))
a = list(str(num))   #将一个整数的每位数字提取出来
for i in a:
    print(i, end=" ")

