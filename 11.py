class cenius:
    def __init__(self,value=20.0):
        print('init')
        self.value=float(value)

    def __get__(self,instance,owner):
        print('cel_get')
        return self.value

    def __set__(self,instance,value):
        print('cel_set')
        self.value=float(value)

class Huashi:
    def __get__(self,instance,oener):
        print('huashi_get')
        return instance.cel*1.8+32

    def __set__(self,instance,value):
        print('huashi_set')
        instance.cel=(float(value)-32.0)/1.8

class Temp:
    cel=cenius()
    huashi=Huashi()


