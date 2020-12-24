#ip被封了  卒

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DongguanItem

class SunSpider(CrawlSpider):
    name = 'sun'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/political/index/politicsNewest?id=1&page=1']

    rules = (
        Rule(LinkExtractor(allow=r'id=1&page=\d+'), follow=True),
        Rule(LinkExtractor(allow=r'index\?id=\d+'), callback='parse_item2'),
    )

    def parse_item1(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item

    def parse_item2(self, response):
        item=DongguanItem()
        item['url']=response.url
        item['title']=response.xpath("//div[@class='mr-three']/p/text()").extract_first()
        item['no']=response.xpath("//div[@class='mr-three']//span[4]").extract_first().split('：')[-1]
        item['text']=response.xpath("//div[@class='details-box']/pre/text()").extract_first()
        print(item)


