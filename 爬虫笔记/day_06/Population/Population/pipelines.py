# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql

class PopulationPipeline:
    def __init__(self):
        # 连接数据库
        self.db = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            passwd="20021112nl",
            db="nl_sql_1",
            charset="utf8")
        # 创建一个数据库游标
        self.cursor = self.db.cursor()
        self.cursor.execute("DROP TABLE IF EXISTS china_population")
        sql = r'''create table china_population(
                   No varchar(10) not NULL ,
                   Province varchar(30) not null,
                   population varchar(50) not null,
                   rise varchar(30) not null
               )'''
        self.cursor.execute(sql)

    def process_item(self, item, spider):
        sql = r'''
            insert into china_population(No,Province,population,rise) values(%s,%s,%s,%s)
            '''
        data=(str(item['No']),str(item['province']),str(item['population']),str(item['rise']))
        self.cursor.execute(sql,data)
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.db.close()
