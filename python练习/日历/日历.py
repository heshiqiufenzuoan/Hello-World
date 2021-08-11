def get_week_with_date(y, m, d):
    if m == 1:
        y -= 1
        m = 13
    elif m == 2:
        y -= 1
        m = 14
    w = (d + 2 * m + 3 * (m + 1) // 5 + y + y // 4 - y // 100 + y // 400) % 7 + 1 
    return w

def is_leap_year(y):
    '''判断一个年份是否为闰年'''
    if y % 400 == 0 or (y % 4 == 0 and y % 100 !=0):
        return True
    else:
        return False

def get_days_in_month(y, m):
    if m in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif m in [4, 6, 11]:
        return 30
    else:
        if is_leap_year(y):
            return 29
        else:
            return 28

'''1. 提示用户输入年月'''
year = int(input("请输入年份："))
month = int(input("请输入月份: "))
'''2. 计算这个月有多少天'''
days = get_days_in_month(year, month)

'''3. 按照指定格式显示日期'''
print("一 二 三 四 五 六 日")
print("-" * 20)
for i in range(1, days + 1):
    w = get_week_with_date(year, month, i)
    if i == 1:
        # 一 0
        # 二 3
        print(f"{' ' * (w - 1) * 3}", end="")
    else:
         if w == 1:
             print("")
    print(f"{i:2d}", end=" ")
print("")