# 多继承
class A:
    def test(self):
        print('A-----的test方法')

    def demo(self):
        print('A-----的demo方法')


class B:
    def demo(self):
        print('B-----的demo方法')
    def test(self):
        print('B-----的test方法')
class C(B, A):
    pass

c = C()
c.test()
c.demo()
'''
若一个子类继承两个父类，
而且两父类的方法一样
此时会调用的一个继承的类的方法,即按继承顺序继承。
'''
# 确定C类对象调用方法的顺序
#__mro__方法, (Methor Resolusion Order)
print(C.__mro__)