import os
import re
import os.path as op
lists=[]
pattern=r'\.jpg$'
tuples=os.walk('D://')
save_path=os.mkdir('D:\\saveimage')

count=1
for item in tuples:
    file=item[0]
    for iitem in item:
        if type(iitem) == type([]):
            for iiitem in iitem:
                file_name=file+'\\'+iiitem
                if(op.isfile(file_name)):
                    if(file_name.endswith('jpg')):
                        save_file_name='D:\\saveimage'+str(count)+'.jpg'
                        count+=1
                        with open(save_file_name,'wb+') as f:
                            f_read=open(file_name,'rb')
                            f.write(f_read.read())
                            f.close()
                            f_read.close()

        else:
            file_name = file +'\\'+ iitem
            if(op.isfile(file_name)):
                if (file_name.endswith('jpg')):
                    save_file_name = 'D:\\saveimage' + str(count) + '.jpg'
                    count += 1
                    with open(save_file_name, 'wb+') as f:
                        f_read = open(file_name, 'rb')
                        f.write(f_read.read())
                        f.close()
                        f_read.close()

