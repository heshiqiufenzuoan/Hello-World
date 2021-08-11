#小明爱跑步
class Person:
    def __init__(self,name,weight):
        #self.属性 = 形参
        self.name = name
        self.weight = weight

    def __str__(self):
        # __str__()必须有返回值
        return"我的名字是 %s 体重是 %.f 公斤" % (self.name,self.weight)

    def run(self):
        print("%s 爱跑步，跑步锻炼身体" % self.name)

    def eat(self):
        print("%s 是吃货，吃完这顿再减肥" % self.name)

xiaoming = Person("小明",65.0)
xiaoming.run()
xiaoming.eat()
print(xiaoming)

#小美爱跑步
xiaomei = Person("小美",50)
xiaomei.eat()
xiaomei.run()
print(xiaomei)