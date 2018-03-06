import os
import os.path
import time
import csv
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3
from mutagen import File

def getID3(str_filename,pathTemp):
    audiofile = MP3(pathTemp, ID3=EasyID3)

    try:
        Album =audiofile['album'][0]
    except:Album=""
    try:
        Title =audiofile['title'][0]
    except:Title=str_filename
    try:
        Artist =audiofile['artist'][0]
    except:Artist=""
    try:
        Albumartist =audiofile['albumartist'][0]
    except:Albumartist=""
    try:
        Date =audiofile['date'][0]
    except:
        Date=""
    t =time.strftime('%Y-%m-%d %X', time.localtime(time.time())) #添加时间
    path =str(os.path.abspath(str_filename))
    path=path.replace('\\','\\\\')
    # print(path)
    try:
        #读取封面
        temppath =os.path.abspath(os.path.dirname(pathTemp))

        afile =File(pathTemp)
        imgfile =afile.tags['APIC:'].data
        img =open(temppath+'\\\\'+Title+'.jpg','wb')
        img.write(imgfile)
        Imgpath = str(os.path.abspath(Title + '.jpg'))
        Imgpath.replace('\\','\\\\')
    except: Imgpath=""

    row=(Title,Artist,Album,Albumartist,Date,path,Imgpath,t)
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
            temp=getID3(str_filename,pathTemp)
            row.append(temp)
        else: pass



def write(row):
    # print(row)
    csvfile = open('music.csv', 'w', newline="", encoding='utf-8')
    write = csv.writer(csvfile)
    tfile =open('music.txt','w',encoding='utf-8')
    for n in row:
        write.writerow(n)
        for k in n:
            tfile.write(str(k)+'\t')
        tfile.write('\n')
        #print(n,end='\n',flush="false")
    csvfile.close()
    tfile.close()
