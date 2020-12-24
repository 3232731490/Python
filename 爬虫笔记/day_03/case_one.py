from lxml import etree
import  urllib.request as ur
import json


class DoubanSpider:
    def __init__(self,begin, end, url):
        self.pagebegin=int(begin)
        self.pageend=int(end)
        self.url=url
        self.headers={'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E'}

    def downloadpage(self, i):
        fullurl=self.url+str(i)
        request = ur.Request(fullurl, headers=self.headers)
        html = ur.urlopen(request).read()
        content=etree.HTML(html)
        url_list=content.xpath('//div[contains(@id, "qiushi_tag_")]')
        for link in url_list:
            print('.', end="")
            username=link.xpath('./div/a/h2')[0].text.strip()
            content=str(link.xpath('.//div[@class="content"]/span/descendant-or-self::text()')).strip().replace("[","").replace(r"\n","").replace("'","").replace(']',"").replace(r'\xa0',"").replace(r'\u200b',"")
            good=link.xpath('.//span/i')[0].text.strip()
            comment=link.xpath('.//span/a/i')[0].text.strip()
            with open("Qiushi.txt", 'a',encoding='utf-8') as f:
                f.write("用户名： " + username + "\n\t内容: " + content + "\n\t点赞数: " + good + "\t评论数: " + comment+"\n\n")
        print()

    def dealPage(self):
        for i in range(self.pageend, self.pagebegin+1):
            print('正在爬取第 ' + str(i)+'页')
            self.downloadpage(i)
            print('第 ' + str(i) +' 页糗事已爬取完毕')

if __name__=='__main__':
    url = "https://www.qiushibaike.com/text/page/"
    begin=input("请输入您要爬取糗事百科的起始页：")
    end=input("请输入您要爬取糗事百科的末尾页: ")
    Spider=DoubanSpider(begin,end,url)
    Spider.dealPage()
