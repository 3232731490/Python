import random
secret=random.randint(1,10)

guess=0
while guess!=secret:
    temp=input("请输入一个数字：")
    guess=int(temp)
    if guess==secret:
        print("猜对了！")
    else :
        if guess<secret:
            print("猜小了！")
        else :
            print("猜大了!")
print("游戏结束！")
