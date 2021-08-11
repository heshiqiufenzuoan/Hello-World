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
        print("向神一样的叫唤")

        Dog.bark(self)
        print("$%^&*#@!%^&^")
'''
如果使用子类调用方法会成为 递归调用
即写成xiaotianquan.bark()
进而出现死循环
'''


xtq = xiaotianquan()
xtq.bark()


'''
RuntimeError: super(): no arguments
运行时错误：super():函数没有参数

本代码出错是因为空格数有错
'''