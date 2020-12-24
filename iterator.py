it = iter("I LOVE YOU")
while True:
    try:
        each=next(it)
    except StopIteration:
        break
    print(each)

class fibs:
    def __init__(self,n=10):
        self.a=0
        self.b=1
        self.n=n
    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if(self.a>self.n):
            raise StopIteration
        return self.a

f=fibs(20)
for i in f:
    print(i,end=" ")