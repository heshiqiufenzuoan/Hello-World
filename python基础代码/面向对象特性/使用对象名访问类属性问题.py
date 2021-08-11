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
fuzi.count = 99
print("工具总数为 %d" % fuzi.count)
print("===> %d" % Tool.count)