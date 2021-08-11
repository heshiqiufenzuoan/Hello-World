year = int(input("请输入一个年份："))
if isinstance(year, int) != True:
    print("请输入一个正确的年份")
else:
    print("判断如下：")

if (year%4) == 0 and (year%100) !=0:
    print("此年为闰年。")
else:
    print("此年为平年。")