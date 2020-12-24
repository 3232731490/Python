import scrapy
from ..items import FlightspiderItem

class FlightSpider(scrapy.Spider):
    name = 'flight'
    allowed_domains = ['flights.ctrip.com']
    url='https://flights.ctrip.com'
    start_urls = [url+'/schedule/']

    #获取每个航班页面  //li/div[@class='m']/a/@href   /schedule/yie..html
        #获取到航班页面后获取所有与该地有关的国内航班  //div[@class='city_m']//li/a/@href   /schedule/yie..html
            #获取每个航班详情  //div[@class='m']/a/@href  /schedule/yie.hrb.html

            #获取航班起始地  //div[@class='tab_m']//ul/li/div[@class='m']/a/text() 格式： 起始-降落   阿尔山-哈尔滨
                #获取航班编号  //td[@class='flight_logo']//strong/text()    CA5889
                #获取起飞时间 //td[@class='depart']/strong[@class='time']/text()  10:30
                #获取降落时间 //td[@class='arrive']/strong[@class='time']/text()  11:40
                #获取价格  //td[@class="price_col"]/span/text()  380

    def parse3(self,response):
        pass
    def parse2(self,response):
        Flight_begin_loc = response.xpath("//div[@class='tab_m']//ul/li/div[@class='m']/a/text()").extract_first()
        print(Flight_begin_loc)
        # if Flight_begin_loc.len()!=0:
        #    item["Flight_begin_loc"]=Flight_begin_loc.split('-')[0]

        Flight_end_loc = response.xpath("//div[@class='tab_m']//ul/li/div[@class='m']/a/text()").extract_first()
        # if Flight_end_loc.len()!=0:
        #    item["Flight_begin_loc"] = Flight_end_loc.split('-')[1]
        print(Flight_end_loc)

        ret3 = response.xpath("//div[@class='tab_m']//ul/li/div[@class='m']/a/text()")
        for each in ret3:
            yield scrapy.Request(str(self.url) + str(each), callback=self.parse3)

    def parse1(self,response):
        ret2 = response.xpath("//div[@class='city_m']//li/a/@href")
        for each in ret2:
            yield scrapy.Request(str(self.url) + str(each), callback=self.parse)

    def parse(self, response):
        #获取到了所有航班页面的url列表
        item=FlightspiderItem()

        ret1 =response.xpath("//li/div[@class='m']/a/@href")
        for each in ret1:
            yield scrapy.Request(self.url+str(each),callback=self.parse1)







        #print(item)



