class Gun:
    def __init__(self, model):
        # 1.枪的型号
        self.model = model
        # 2.子弹的数量
        self.bullet_count = 0

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self):
        # 1.判断子弹数量
        if self.bullet_count <= 0:
            print("[]%s 没有子弹了..." % self.model)
            return
        # 2.发射子弹
        self.bullet_count -= 1
        # 3.提示发射信息
        print("[%s]突突突...[%d]" % (self.model, self.bullet_count))


class Soldier:
    def __init__(self, name):
        # 1.姓名
        self.name = name
        # 2.枪 -- 新兵没有枪
        self.gun = None
    def fire(self):
        #空格后
        #1. 判读士兵是否有枪
        if self.gun == None:
            print("[%s] 没有枪" % self.name)
        return
        #2. 让枪装填子弹
        self.gun.add_buttle(50)

        #3. 高喊口号
        print("[%s] 杀、杀、杀、、、" % self.name)

        #4. 让枪发射子弹
        self.gun.shoot()

# 1. 创建枪对象
ak47 = Gun("AK47")
ak47.add_bullet(50)
ak47.shoot()

# 2.创建许三多
xvsanduo = Soldier("许三多")
xvsanduo.gun = ak47
xvsanduo.fire()
print(xvsanduo.gun)
