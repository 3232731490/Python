#1、计算机的核心是CPU

#2、一个CPU核心一次只能执行一个任务  多个CPU核心可以同时执行多个任务

#3、一个CPU一次只能执行一个进程，其他进程处于非运行状态

#4、进程里包含的执行单元叫做线程     一个进程可以包含多个线程

#5、一个进程的内存空间是共享的，每个进程里的线程都可以使用这些共享空间      一个线程在使用这个空间的时候，必须等待它使用结束，其他线程才可以使用这个空间（通过“锁”实现，防止多个线程使用同一个空间）

#6、进程： 表示程序的依次执行
#   线程： CPU运算的基本调度单位

#GIL： python里的执行通行证，且只有一个，拿到它的线程就可以进入CPU执行任务，没有则等待

#Python的多线程适用于大量密集的IO处理
#Python的多进程适用于大量密集计算

'''
    队列Queue
    import Queue
    常用方法：Queue.qsize()  返回队列大小
            Queue.empty()  返回队列是否为空
            Queue.full()   放回队列是否已满
            Queue.full 与maxsize 大小对应
            Queue.get(block[,timeout])  获取队列，timeout--等待时间

            myqueue=Queue.Queue(maxsize=num)   创建一个队列对象
            myqueue.put(value)  将元素放入队列中
            myqueue.get()  从队列中取出元素
'''

#导入线程库
import threading as th
#队列
from queue import Queue
#解析库
from lxml import etree
#请求处理
import requests
#json文件处理
import json

import urllib.request as ur

class ThreadCraw(th.Thread):
    def __init__(self, threadname, pagequeue,dataqueue):
        #调用父类构造函数的两种方法
        #th.Thread.__init__(self)
        super(ThreadCraw, self).__init__()
        #线程名
        self.threadname=threadname
        #页码队列
        self.pagequeue=pagequeue
        #数据队列
        self.dataqueue=dataqueue
        self.url = "https://www.qiushibaike.com/text/page/"
        self.headers={'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E'}
    def run(self):
        print("启动  "+self.threadname)
        while not CRAL_EXIT:
            #取出一个数字页码
            #get中的可选参数block，默认值为True 其作用：1、若队列为空，block为True则进入阻塞状态，直到队列有新数据
            #                                     2、如果队列为空，block为False则弹出队列为空异常

            try:
                page=self.pagequeue.get(False)
            except:
                pass

            #组合完整url地址
            fullurl=self.url+str(page)+'/'

            #发送请求
            #request = ur.Request(fullurl, headers=self.headers)
            #html = ur.urlopen(request).read()
            
            content=requests.get(fullurl,headers=self.headers)
            html=content.text
            self.dataqueue.put(html)
        print("结束 "+self.threadname)


class ThreadParse(th.Thread):
    def __init__(self, threadname, dataqueue, Filename):
        super(ThreadParse, self).__init__()
        #线程名
        self.threadname=threadname
        #数据队列
        self.dataqueue=dataqueue
        #保存解析后数据文件名
        self.Filename=Filename

    def run(self):
        print("启动 "+self.threadname)
        while not PARSE_EXIT:
            try:
                data=self.dataqueue.get(False)
                self.parse(data)
            except:
                pass
        print("结束 " + self.threadname)

    def parse(self,data):
        content=etree.HTML(data)
        url_list = content.xpath('//div[contains(@id, "qiushi_tag_")]')
        for link in url_list:
            username = link.xpath('./div/a/h2')[0].text.strip()
            content = str(link.xpath('.//div[@class="content"]/span/descendant-or-self::text()')).strip().replace("[","").replace(r"\n", "").replace("'", "").replace(']', "").replace(r'\xa0', "").replace(r'\u200b', "")
            good = link.xpath('.//span/i')[0].text.strip()
            comment = link.xpath('.//span/a/i')[0].text.strip()
            with open(self.Filename,'a') as f:
                f.write(json.dumps(("用户名： " + username + "  内容: " + content + "  点赞数: " + good + "  评论数: " + comment + "  "), ensure_ascii=False)+'\n\n')

#采集线程退出循环标记
CRAL_EXIT=False
#解析线程退出循环标记
PARSE_EXIT=False

def main():
    #页码队列，可以存储十个页面
    pagequeue=Queue(maxsize=10)

    #放入了十个数字  先进先出
    for i in range(1,11):
        pagequeue.put(i)

    #采集结果（每一个网页的HTML源码）的队列，参数为空表示无限制
    dataqueue=Queue()

    #要保存到的本地文件名
    Filename="duanzi.json"

    #三个线程的名字
    crawlist=["采集线程1号","采集线程2号","采集线程3号"]

    threadcraw=[]

    for threadname in crawlist:
        thread=ThreadCraw(threadname, pagequeue, dataqueue)
        thread.start()
        #存储三个采集线程
        threadcraw.append(thread)

    #三个解析线程的名字
    parsequeue=["解析线程1号","解析线程2号","解析线程3号"]

    #存储三个解析线程的列表
    threadparse=[]

    for threadname in parsequeue:
        thread=ThreadParse(threadname, dataqueue, Filename)
        thread.start()
        #存储三个解析线程
        threadparse.append(thread)

    #只要页码队列不为空，则一直在此等待
    while not pagequeue.empty():
        pass

    #页码为空后，将采集线程退出循环
    global CRAL_EXIT
    CRAL_EXIT=True

    print("pagequeue为空！")

    #只要数据队列不为空，则一直在此等待
    while not dataqueue.empty():
        pass

    global PARSE_EXIT
    PARSE_EXIT=True

    print("dataqueue为空！")

    #添加阻塞 防止当主线程执行结束时，采集线程还未执行结束就跟着结束
    for thread in threadcraw:
        thread.join()
        print("1")

    for thread in threadparse:
        thread.join()
        print('2')

if __name__=="__main__":
    main()

