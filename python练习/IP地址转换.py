def func(x):
    lis = x.strip().split('.')
    li = [bin(int(i)) for i in lis]
    li2 = [i.replace('0b',(10-len(i))*'0') for i in li]
    return int(''.join(li2), 2)

ret = func('10.3.9.12')

print(ret)