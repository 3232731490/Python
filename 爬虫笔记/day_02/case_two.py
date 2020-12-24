import urllib.request as ur
import urllib.parse as up
from lxml import etree
import os
class GirlSpider:
    def __init__(self,theme, begin, end):
        self.pagebegin = begin
        self.pageend = end
        self.theme = up.quote(theme, encoding="utf-8")
        #加headers会找不到目标地址，原因应该是不同浏览器的查找元素路径不同
       # self.headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.55'}

    def dealurl(self):
        url="https://tieba.baidu.com/f?kw="+self.theme+"&pn="
        for i in range(self.pageend-self.pagebegin+1):
            fullurl=url+str(i*50)
            print("正在下载第" +str(i+1)+ "页")
            self.loadpage(fullurl, i+1)
        print("下载完毕，谢谢使用！")

    def loadpage(self,url ,page):
        #request=ur.Request(url, headers=self.headers)
        request=ur.Request(url)
        html=ur.urlopen(request).read()
        content=etree.HTML(html)
        url_list=content.xpath('//div/div/div/div[@class="threadlist_title pull_left j_th_tit "]/a[@rel="noreferrer"]/@href')
        for item in url_list:
            self.loadImage(item, page)

    def loadImage(self,url , page):
        fullurl="https://tieba.baidu.com"+url
        #request = ur.Request(fullurl, headers=self.headers)
        request = ur.Request(fullurl)
        html = ur.urlopen(request).read()
        content = etree.HTML(html)
        url_list=content.xpath('//div/img[@class="BDE_Image"]/@src')
        for item in url_list:
            self.write_Image(item, page)

    def write_Image(self, url, page):
        #request=ur.Request(url, headers=self.headers)
        request = ur.Request(url)
        Filename=url[-10:]
        print("\t正在下载： "+Filename)
        src="C:\\Users\\32327\\Desktop\\Python\\爬虫笔记\\day_02\\GirlImage\\第"+str(page)+"页"
        if(not os.path.exists(src)):
            os.mkdir(src)
        Filename = src+"\\" + Filename
        image=ur.urlopen(request).read()
        with open(Filename, 'wb') as f:
            f.write(image)

if __name__=="__main__":
    theme=input("请输入您要爬取哪个板块的图片： ")
    pagebegin=int(input("请输入您要爬取的起始页："))
    pageend=int(input("请输入您要爬取的结束页："))
    spider=GirlSpider(theme,pagebegin,pageend)
    spider.dealurl()

