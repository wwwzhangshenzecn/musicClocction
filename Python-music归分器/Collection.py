'''
Author:zhangze
Place:WIT_636
Time:2018/1/17
function:分类音乐文件
'''
import os
import os.path
import time
def CollectMusic(path,rootPath,loseList=[],count=[0]):
    '''
    :param path: 需要整理的目录
    :param rootPath: 需要存放的目录
    :param loseList: 失败列表
    :param count: 成功计数
    :return: NONE
    '''
    fileList = os.listdir(path) # 获取目录下的所有文件

    for filename in fileList:
        str_filename = str(filename)
        index = str_filename.find('-')
        if index <=1:#防止出现无名称文件夹
            index = 2

        pathTemp = os.path.join(path,filename) #加入文件名组成路径
        if os.path.isdir(pathTemp): # pathTemp是目录，进行迭代
            CollectMusic(pathTemp,rootPath,loseList,count)
        elif str_filename[-4:].lower() == ".mp3": #判定MP3文件
            startNamePath = str_filename[:index-1] #提取MP3文件名字

            startPath =  os.path.join(rootPath,startNamePath)
            if os.path.exists(startPath):
                #print("已存在文件夹%s:" %str(startPath))
                pass
            else:
                os.mkdir(startPath) # 创造歌手的文件
                #print("创建文件夹%s:" %str(startPath))
            try:
                sourcePath = os.path.join(path,filename)
                #print("1----",sourcePath)
                targetPath = os.path.join(startPath,filename)
                #print("2----",targetPath)
                if os.path.isfile(sourcePath):
                    music_read = open(sourcePath,"rb+").read()#复制文件
                    music_write = open(targetPath,"wb+", os.O_RDWR | os.O_CREAT)

                    if os.path.exists(targetPath): # 确认目标文件存在
                        music_write.write(music_read)
                        print("%d转移成功%s" %( (count[0]+1),filename))
                        try:
                            count[0] +=1
                            os.remove(sourcePath)
                            print("移除成功：",filename)
                        except: pass
                    else:
                        print("%d转移失败%s" %(len(loseList),filename))
                        loseList.append(filename)
            except:
                print("转移失败%s：" %filename)
                loseList.append(filename)



def Collection(copyPath,rootPath,loseList=[],count=[0]):
    start = time.time()
    CollectMusic(copyPath, rootPath, loseList, count)
    print("归总失败列表：")
    end = time.time()
    for list in loseList:
        print(list)
    print("归总成功：", count[0])
    print("归总失败：%f" % len(loseList))
    print("归总耗时：%f" % (end - start))

