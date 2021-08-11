x = 16
y = 20
for i in range(1, 16):
    if ((x % i == 0) and (y % i == 0)):
        hcf = i
        print(hcf)