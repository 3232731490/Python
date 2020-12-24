class Mylist:
    def __init__(self,*args):
        self.value=[x for x in args]
        self.count={}.fromkeys(range(len(self.value)),0)
    def __len__(self):
        return len(self.value)

    def __getitem__(self,key):
        self.count[key]+=1
        return self.value[key]

c1=Mylist(1,3,5,6,7)
print(c1[1])