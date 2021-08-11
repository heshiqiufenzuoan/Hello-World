# 儿子拥有父亲的属性和方法，同时也拥有爷爷的属性和方法
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
    def bark(self):
        print("汪汪叫。。。")


class xiaotianquan(Dog):
    def fly(self):
        print("我会飞、、、")
    def bark(self):
        print("叫的跟驴一样")

xtq = xiaotianquan()
xtq.bark()
'''
如果在子类中重写了父类的方法
在调用的时候会执行子类重写的方法。
'''