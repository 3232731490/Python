# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DongguanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #链接
    url = scrapy.Field()

    #标题
    title =scrapy.Field()

    #编号
    no=scrapy.Field()

    #内容
    text= scrapy.Field()
