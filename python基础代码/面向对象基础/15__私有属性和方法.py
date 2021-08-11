'''
本段代码为私有属性和方法的有关代码；
代码之所以不能运行是因为age已经被私有化，即变成了__age
'''
class Women:
    def __init__(self,name):
        self.name = name
        self.__age = 23

    def __secret(self):
        # 在对象的方法内部是可以访问对象的私有属性的。
        print("%s 的年纪是 %s" % (self.name,self.__age))

xiaofang = Women("小芳")

#私有属性，在外界不能被直接访问
# print(xiaofang.__age)

#私有方法同样不能被外界直接访问
xiaofang.__secret()