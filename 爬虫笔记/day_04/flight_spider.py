import urllib.request as ur
from lxml import etree
import json
import jsonpath

class Flight:
    def __init__(self):
        self.url='https://flights.ctrip.com'
        self.headers={"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.60"}
        self.location_begin=""
        self.location_end=""
        self.flightno=""
        self.flighttime_beigin=""
        self.flighttime_end=""
        self.flightprice=""
        self.Filename="flight.json"

    def urlparse(self):
        request=ur.Request(self.url+'/schedule/',headers=self.headers)
        response=ur.urlopen(request)
        html=response.read()
        #print(html.decode("utf-8"))
        content=etree.HTML(html)
        url_list=content.xpath("//li/div[@class='m']/a/@href")
        for each in url_list:
            self.flighturl(each)
    def flighturl(self,url1):
        fulurl=self.url+url1
        request = ur.Request(fulurl, headers=self.headers)
        response = ur.urlopen(request)
        html = response.read()
        content = etree.HTML(html)
        url_list = content.xpath("//div[@class='city_m']//li/a/@href")
        for each in url_list:
            self.filgturlparse(each)

    def filgturlparse(self,url1):
        fulurl=self.url+url1

        request = ur.Request(fulurl, headers=self.headers)
        response = ur.urlopen(request)
        html = response.read()
        content = etree.HTML(html)
        url_list = content.xpath("//div[@class='m']/a/@href")
        for each in url_list:
            self.location_begin = content.xpath("//div[@class='tab_m']//ul/li/div[@class='m']/a/text()")[0].split("-")[0]
            self.location_end=content.xpath("//div[@class='tab_m']//ul/li/div[@class='m']/a/text()")[0].split("-")[1]
            self.flightinfoparse(each)

    def flightinfoparse(self,url):
        fulurl=self.url+url
        #print(fulurl)
        request = ur.Request(fulurl, headers=self.headers)
        response = ur.urlopen(request)
        html = response.read()
        #print(html.decode("utf-8"))
        content = etree.HTML(html)
        #print(content)
        flightno_list=content.xpath("//td[@class='flight_logo']//strong")
        #print(flightno_list)
        flighttime_begin_list=content.xpath("//td[@class='depart']/strong[@class='time']/text()")
        flighttime_end_list=content.xpath("//td[@class='arrive']/strong[@class='time']/text()")
        flightprice_list=content.xpath("//td[@class='price_col']/span/text()")
        for i in range(len(flightno_list)):
            self.flightno=flightno_list[i]
            self.flighttime_beigin=flighttime_begin_list[i]
            self.flighttime_end=flighttime_end_list[i]
            self.flightprice=flightprice_list[i]
            self.loadsInfo()

    def loadsInfo(self):
        with open(self.Filename,"w") as f:
            text=json.dumps(self.flightno+" "+self.flighttime_beigin+" "+self.flighttime_end+" "+self.location_begin+" "+self.location_end+" "+self.flightprice)
            f.write(text)

if __name__=="__main__":
    flightspider=Flight()
    flightspider.urlparse()