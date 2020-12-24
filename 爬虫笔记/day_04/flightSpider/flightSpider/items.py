# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FlightspiderItem(scrapy.Item):
    # define the fields for your item here like:
    #航班编号
    FlightNo = scrapy.Field()

    #起始地点
    Flight_begin_loc=scrapy.Field()

    #降落地点
    Flight_end_loc=scrapy.Field()

    #起飞时间
    Flight_begin_time=scrapy.Field()

    #降落时间
    Flight_end_time=scrapy.Field()

    #航班票价
    Flight_price=scrapy.Field()

    #航班折扣
    Flight_disc=scrapy.Field()

    #航班最大人数
    Flight_maxsize=scrapy.Field()

    #航班当前人数
    Flight_nowcap=scrapy.Field()


