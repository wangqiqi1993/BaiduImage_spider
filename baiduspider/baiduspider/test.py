import os
import shutil
rollback_1=r'E:\MT\20190506\allbody\completed\rollback_1'
error=r'C:\Users\486\Pictures\complex'
data=r'E:\MT\20190506\allbody\completed\correcct\data'
for file in os.listdir(error):
    name=file.split('.')[0]
    shutil.move(os.path.join(data,file),rollback_1)
    shutil.move(os.path.join(data, name+'.json'), rollback_1)
    shutil.move(os.path.join(data, name+'_mask.bmp'), rollback_1)