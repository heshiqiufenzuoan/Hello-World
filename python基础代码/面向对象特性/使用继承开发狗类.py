'''
狗类是动物类的子类、动物类是狗类的父类、狗类从动物类中继承
狗类是动物类的派生类、动物类是狗类的基类、狗类从动物类中派生
'''
class Animal:

    def eat(self):
        print("吃、、、")

    def drink(self):
        print("喝、、、")

    def run(self):
        print("跑、、、")

    def sleep(self):
        print("睡、、、")

class Dog(Animal):
    #子类有父类的所有属性和方法
    def bark(self):
        print("汪汪汪、、、")

class XiaoTianQuan(Dog):
    def fly(self):
        print('我会飞/')

xtq = XiaoTianQuan()
xtq.fly()
xtq.run()
