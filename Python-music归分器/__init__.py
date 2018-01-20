from Collection import Collection
'''
rootPath:需存放的音乐文件夹
copuPath:需整理的音乐文件夹
Author:zhangze
Place:WIT_636
Time:2018/1/17
function:分类音乐文件
'''
if __name__ == "__main__":
    rootPath = "G:\\Music\\"  # 存放文件夹
    copyPath = "G:\\newMusic\\"  # 整理文件夹
    loseList = []
    count = [0]
    Collection(copyPath,rootPath,loseList,count)

    while True:
        n = str(input("输入 exit 退出："))
        if n == "exit":
            exit()

