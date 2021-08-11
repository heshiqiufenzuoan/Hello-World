'''属性的获取机制---向上寻找'''
class Tool(object):
    count = 0

    def __init__(self, name):
        self.name = name

        # 让类的值加一
        Tool.count += 1


chiuzi = Tool("锤子")
fuzi = Tool("斧子")
shiutong = Tool("水桶")

# 输出工具数量
# print(Tool.count)
print("工具总数为 %d" % fuzi.count)