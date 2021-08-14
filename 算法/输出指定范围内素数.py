lower = int(input("输出区间最小值："))
upper = int(input("输出区间最大值："))
print("该区间范围内素数有:", end=" ")
for num in range(lower, (upper+1)):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
    else:
        print(num, end=" ")