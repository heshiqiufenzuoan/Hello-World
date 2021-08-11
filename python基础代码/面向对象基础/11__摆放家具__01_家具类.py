class HouseItem:
    def __init__(self,name,area):
        self.name = name
        self.area = area
    def __str__(self):
        return "[%s] 占地 %.2f" % (self.name,self.area)

#创建家具
bed = HouseItem("西蒙斯",4)
chest = HouseItem("衣柜",2.5)
table = HouseItem("餐桌",2)

print(bed)
print(chest)
print(table)