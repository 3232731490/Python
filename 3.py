def function(x):
    if x<0:
        return 0
    elif x<=5:
        return x
    elif x<10:
        return 3*x-5
    elif x<20:
        return x/2-2
    else:
        return 0

x=float(input("请输入一个数："))
print('f('+str(x)+') =' +str(function(x)))