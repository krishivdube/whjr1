import os
import shutil
path=input("Enter Directory Name")
list_of_files=os.listdir(path)
for file  in list_of_files:
    name,ext=os.path.splitext(path)
    ext=ext[1:]
    if ext=='':
        continue
    if os.path.exists(path+'/'+ext):
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
    else:
        os.mkdir(path+'/'+ext)
        shutil.move(path+'/'+file,path+'/'+ext+'/'+file)
        
