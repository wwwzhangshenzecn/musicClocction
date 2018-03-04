from  music_csv import *
import  os
if __name__=='__main__':
    path=os.path.abspath(os.path.dirname(__file__))
    print(path)
    row=[]
    getMusicinfo(path,row)
    write(row)
