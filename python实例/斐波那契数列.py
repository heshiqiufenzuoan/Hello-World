num = int(input("你需要斐波那契数列的前几项，请输入："))
if num < 0:
    print("您输入的格式不正确，请重新输入。")
elif num == 1:
    print("0")
elif num == 2:
    print("0, 1")
elif num == 3:
    print("0, 1, 1")
else:
    print("0 , 1 , 1 ,", end=" ")
    n1 = 0
    n2 = 1
    n = 3 #第三个
    count = 1
    while n < num:
        n += 1
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        count = n1 + n2
        print(count, ",", end=" ")