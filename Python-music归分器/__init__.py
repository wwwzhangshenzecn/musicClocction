from Collection import Collection
import os
'''
将本文件放入需整理的文件夹中，运行即可。
Author:zhangze
Place:WIT_636
Time:2018/1/17
function:分类音乐文件
'''
if __name__ == "__main__":
    # rootPath = "G:\\Music\\"  # 存放文件夹
    rootPath = os.path.abspath(os.path.dirname(__file__))
    copyPath = os.path.abspath(os.path.dirname(__file__))
    # copyPath = "G:\\newMusic\\"  # 整理文件夹
    loseList = []
    count = [0]
    Collection(copyPath,rootPath,loseList,count)

    while True:
        n = str(input("输入 exit 退出："))
        if n == "exit":
            exit()

