import os
import os.path
import time
import csv


def getID3(str_filename):
    index = str_filename.find('-')
    if index <= 1:  # 防止出现无名称文件夹
        index = 2
    author = str_filename[:index - 1]  # 提取MP3歌手
    name = str_filename[index+2:-4] #歌曲名
    t =time.strftime('%Y-%m-%d %X', time.localtime(time.time()))
    path =str(os.path.abspath(str_filename))
    path=path.replace('\\','\\\\')
    print(path)
    row=(name,author,path,t)
    return row

def getMusicinfo(path,row):
    '''
    :param path: MP3   文件存放的目录
    :param count:  收集数量
    :return: NULL
    '''

    temppath = os.path.abspath(path)
    print(temppath,end="\n")
    file = os.listdir(temppath) #获取此目录下的所有文件（包括目录）
    for filename in file:
        str_filename = str(filename)

        pathTemp = os.path.join(path,filename) #组成新的文件路劲

        if os.path.isdir(pathTemp):
           getMusicinfo(pathTemp,row)
        elif filename[-4:].lower() == '.mp3':
            temp=getID3(str_filename)
            row.append(temp)
        else: pass



def write(row):
    # print(row)
    csvfile = open('music.csv', 'w', newline="", encoding='utf-8')
    write = csv.writer(csvfile)
    write.writerow(('Name', 'Author','Path','Time'))
    for n in row:
        write.writerow(n)
        print(n,end='\n',flush="false")
    csvfile.close()

