import pickle
file_open=open('ceshi.txt','wb')
pickle.dump([1,2,3,4,5],file_open)
file_open.close()

file_r=open('ceshi.txt','rb+')
b=pickle.load(file_r)
print(b[1])
