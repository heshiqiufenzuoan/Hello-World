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


class Cat(Animal):
    def catch(self):
        print('抓老鼠')


# 创建一个哮天犬对象
xtq = xiaotianquan()
xtq.fly()
xtq.run()
xtq.bark()

xtq.catch()
'''
不能运行是因为xtq类继承Dog类，
Cat类继承Animal类，
两类没关系
'''
