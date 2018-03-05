from  music_csv import *
import  os

'''
将本文件夹中的所有音乐文件扫描，输出为csv格式列表

'''
if __name__=='__main__':
    path=os.path.abspath(os.path.dirname(__file__))
    print(path)
    row=[]
    getMusicinfo(path,row)
    write(row)

    while(1):
        temp =input("输入exit退出：")
        if(temp == 'exit'):
            exit(0)
