class MusicPlayer(object):
    def __new__(cls, *args, **kwargs):
        #1. 使用类名创建对象的时候，new方法会被自动调用
        print('创建对象，分配空间')
        '''
        :param args:一颗星 多值的元组参数
        :param kwargs: 两颗星多值的字典参数
        :return:
        '''
        # 2.为对象分配空间
        instance = super().__new__(cls)
        #3. 返回对象的引用
        return instance
    def __init__(self):
        print("播放器初始化")

# 创建播放器对象
player = MusicPlayer()
print(player)