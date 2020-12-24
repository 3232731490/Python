# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentspiderItem(scrapy.Item):
    # define the fields for your item here like:

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

