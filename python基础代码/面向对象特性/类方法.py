class Tool(object):
    count = 0
    @classmethod
    def show_tool_count(cls):
        print("工具数量的对象 %d" % cls.count)

    def __init__(self, name):
        self.name = name

        # 让类的值加一
        Tool.count +=1

# 创建工具对象
tool1 = Tool("锤子")
tool2 = Tool("斧子")

#调用类方法
Tool.show_tool_count()
#创建类方法