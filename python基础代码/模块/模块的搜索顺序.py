import random
rand = random.randint(0,10)
print(rand)

'''
1. __name__属性：一个模块被一个程序引入的时候，其主程序将运行。如果我们想在模块被引入时，模块中的某一程序块不执行，可以使用
__name__属性来使该程序块仅仅在执行模块自生时运行。
'''
# 例：
if __name__ == '__main__':
    print("程序自身在执行。")
else:
    print("来自另外一个模块。")