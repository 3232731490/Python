import scrapy
from ..items import *


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    url='https://careers.tencent.com/search.html?query=ot_40001001,ot_40001002,ot_40001003,ot_40001004,ot_40001005,ot_40001006&index='
    offset=1
    start_urls =[url+str(offset)]

    def parse(self, response):
        #response和在浏览器上的不一样
        #print(response.text)

        ret=response.xpath("//div[@class='recruit-list']")

        for each in ret:
            #初始化模型对象

            item=TencentspiderItem()

            '''
    #职位名
    name = scrapy.Field()

    #工作简介
    recommend=scrapy.Field()

    #职位类别
    type=scrapy.Field()

    #工作地址
    position=scrapy.Field()

    #发布时间
    time=scrapy.Field()
            '''
            item['name']=each.xpath("./a/h4/text()").extract_first()
            item['position']=each.xpath("./a/p[1]/span[2]/text()").extract_first()
            item['type']=each.xpath("./a/p[1]/span[3]/text()").extract_first()
            item['time']=each.xpath("./a/p[1]/span[4]/text()").extract_first()
            item['recommend']=each.xpath("./a/p[2]/text()").extract_first()

            #将数据交给管道文件处理
            yield item

        if self.offset <= 3:
            self.offset += 1
        # 处理完一页数据后重新发送下一页请求，将请求重新发送给调度器 （入队列，出队列，交给下载器下载）同时拼接为新的url，并使用回调函数self.parse处理response  如果是重复请求则不会再发送给调度器
        yield scrapy.Request(self.url + str(self.offset), callback=self.parse)



