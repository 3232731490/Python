
def function1():
    '这是第一个函数的帮助文档'
    global num1
    print('随便打印')
    print('全局变量num1: ', num1)
    num1+=10
    return 1

def function2(X):
    def function3(Y):
        return X +Y
    return function3

num1=10

function1()
help(function1)
print('函数中修改后全局变量num1: ', num1)
print('闭包：')
print('\t',function2(2)(3))

print('lambda表达式：')
g=lambda X : X*2
print(g(2))

print(list(filter(None,[True,False,True])))

print(list(filter(lambda X : not X,[True,False,True])))

print(list(map(lambda X :X*2,[1,2,3,4])))
