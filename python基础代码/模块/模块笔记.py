'''
1. 导入包的方式：
    import A as B ：意思就是把A模块重新命名为B（即视为B模块；)
    import A from B : 意思就是导入模块A中的B工具，也是从模块中导入一个指定的部分到当前的命名空间去。
    from A import*:把一个模块中的所有项目全部导入。
2. 如果两个模块中哦都有同一个函数，则后导入的函数会覆盖先导入的函数
3. 若解决2中的问题，则需要使用1 中的方法，通过改名字使用别名方法来解决问题
4. from A import* : 导入A中的所有工具。
  注意：尽量不要使用这种方式，出现问题不容易排查。
5.搜索路径被存储在sys模块中的path变量，在我的电脑中，结果如下：
['', 'D:\\software\\Python\\Python-3.8.2\\python38.zip',
'D:\\software\\Python\\Python-3.8.2\\DLLs',
'D:\\software\\Python\\Python-3.8.2\\lib',
'D:\\software\\Python\\Python-3.8.2',
'D:\\software\\Python\\Python-3.8.2\\Lib\\site-packages']
解释：第一个是空目录，代表当前路径，即解释器的的目录。
'''
'''

'''