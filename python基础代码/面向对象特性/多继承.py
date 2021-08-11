# 多继承
class A:
    def Itname(self):
        print('学习多继承')

class B:
    def Itrun(self):
        print('多继承中的第二个继承')

class C(A, B):
    pass

c = C()
c.Itname()
c.Itrun()