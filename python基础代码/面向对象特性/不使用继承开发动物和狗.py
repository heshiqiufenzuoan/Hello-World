class Animal:

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")


class Dog:
    def __init__(self,name):
        self.name = name

    def eat(self):
        print("吃")

    def drink(self):
        print("喝")

    def run(self):
        print("跑")

    def sleep(self):
        print("睡")

    def drak(self):
        print("咬")

xiaogou = Dog('wangcai')
xiaogou.run()
xiaogou.eat()
xiaogou.drink()
xiaogou.sleep()
xiaogou.drak()
