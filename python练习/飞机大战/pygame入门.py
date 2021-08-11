import pygame

pygame.init()
# 创建游戏窗口


screen = pygame.display.set_mode((393,700))
#初始化游戏显示窗口


#绘制背景图像
#1. 使用load（）方法加载图像数据
bg = pygame.image.load("./Plane/3.jpg")
#2. blit绘制图像
screen.blit(bg, (0, 0))#(0,0)表示绘制图像的位置
#3. update更新屏幕显示
pygame.display.update() #可统一调用，提高效率，提高游戏运行速度

#绘制英雄飞机
hero = pygame.image.load("./Plane/空白.jpg")
screen.blit(hero, (150,600 ))#(0,0)表示绘制图像的位置
pygame.display.update()


#创建时钟对象
clock = pygame.time.Clock()
# 1.定义rect类型变量记录飞机初始位置
hero_rect = pygame.Rect(150, 300, 102, 126)#前两表示坐标，后两大小
while True:
    clock.tick(60)
    #捕获事件
    event_list = pygame.event.get()
    if len(event_list) > 0:

        print(event_list)
#2. 修改飞机位置
    hero_rect.y -= 5
    #判断飞机位置
    if hero_rect.y <= 0:
        hero_rect.y = 700

#3.调用blit绘制图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)
#4.调用update更新显示
    pygame.display.update()
# 无限循环的作用，就是为了让游戏窗口一直循环存在不关闭

pygame.quit()
