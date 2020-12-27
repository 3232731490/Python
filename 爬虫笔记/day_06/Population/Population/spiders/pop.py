import scrapy


class PopSpider(scrapy.Spider):
    name = 'pop'
    allowed_domains = ['www.maigoo.com']
    start_urls = ['https://www.maigoo.com/news/488659.html']


    def parse(self, response):
        odd_list=response.xpath('//div[@class="mod_body"]//tr[@class="md_tr font14 bgcolor"]/td[@class="md_td"]/text()').extract()
        dob_list=response.xpath('//div[@class="mod_body"]//tr[@class="md_tr font14 bgcolor-s"]/td[@class="md_td"]/text()').extract()
        odd_item={}
        dob_item={}

        for i in range(16):
            j=i*4
            odd_item["No"] =odd_list[j]
            odd_item["province"] =odd_list[j+1]
            odd_item["population"] =odd_list[j+2]
            odd_item["rise"] =odd_list[j+3]
            yield odd_item
           # print(odd_item)

            if i < 15:
                dob_item["No"] = dob_list[j]
                dob_item["province"] = dob_list[j + 1]
                dob_item["population"] = dob_list[j + 2]
                dob_item["rise"] = dob_list[j + 3]
                yield dob_item
             #   print(dob_item)
