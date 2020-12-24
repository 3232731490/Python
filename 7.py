f=open('C:\\Users\\32327\\Desktop\\Python\\文件读写测试\\communi.TXT','r',encoding='UTF-8')
fw1=open('C:\\Users\\32327\\Desktop\\Python\\文件读写测试\\A.txt','w',encoding='UTF-8')
fw2=open('C:\\Users\\32327\\Desktop\\Python\\文件读写测试\\B.txt','w',encoding='UTF-8')

for each in f:
    str1=str(each)
    str2=str1.split(':')
    if str1.startswith('A:'):
        fw1.write(str2[1])
    elif str1.startswith('B:'):
        fw2.write(str2[1])
    else:
        print(each)
fw1.close()
fw2.close()
f.close()
