# 绘制五角星
from turtle import *
fillcolor("red")
begin_fill()
while True:
    forward(150)
    right(144)
    if distance(0, 0) < 1:
        break
end_fill()
done()

'''================================================================================='''

# 绘制圆
import turtle
turtle.pensize(2)
turtle.circle(10)
turtle.circle(20)
turtle.circle(30)
turtle.circle(40)
turtle.circle(50)

'''
import turtle是导入整个包，不能使用为声明的变量，因此，在每一项前都要加上前缀；
而from turtle import * 是未导入包，但从这个命名空间导入了所有成员，所以直接使
用命名空间内已知的项目即可，比如：pen、turtle。
'''