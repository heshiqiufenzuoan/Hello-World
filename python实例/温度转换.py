Celsius = float(input("请输入摄氏度："))
fahrenheit = float(input("请输入华氏度："))
Celsius_fahrenheit = (Celsius * 1.8) + 32
fahrenheit_Celsius = (fahrenheit - 32) / 1.8
print("%s 对应的华氏度为：%.2f" %(Celsius, Celsius_fahrenheit))
print("%s 对应的华氏度为：%.2f" %(fahrenheit, fahrenheit_Celsius))
