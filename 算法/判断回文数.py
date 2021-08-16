'''
回文数是指从左到右和从右到左都一样的整数
'''
x = int(input("请输入一个整数："))
def isPalindrome(x):
    if x < 0:
        return False
    else:
        x = str(x)
        if x == x[::-1]:
            return True
        else:
            return False
b = isPalindrome(x)
print(b)