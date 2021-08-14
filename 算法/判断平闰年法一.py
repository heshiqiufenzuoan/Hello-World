year = int(input("请输入一个年份："))
if isinstance(year, int) != True:
    print("请输入一个正确的年份")
else:
    print("判断如下：")

if (year%4) == 0 and (year%100) !=0:
    print("此年为闰年。")
elif (year%400) ==0:
    print("此年为闰年。")
else:
    print("此年为平年。")
'''
判断平闰年方法：
除以100余数不等于0，除以4余数等于0为闰年或者直接除以400余数为0为闰年。
否则为平年。
'''
