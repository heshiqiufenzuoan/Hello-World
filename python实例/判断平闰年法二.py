import calendar
year = int(input("请输入一个年份："))
value = calendar.isleap(year)
if value == True:
    print("%s为闰年" % (year))
else:
    print("%s为平年" % (year))
