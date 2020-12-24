import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import FlightTestItem

class FlightSpider(CrawlSpider):
    name = 'flight'
    allowed_domains = ['flight.ctrip.com']
    start_urls = ['http://flight.ctrip.com/schedule/']

    rules = (
        Rule(LinkExtractor(allow=r'//flights.ctrip.com/itinerary/oneway/SHA-TSN?'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = FlightTestItem()
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        item['Flight_begin_loc']=response.xpath('')
        return item
