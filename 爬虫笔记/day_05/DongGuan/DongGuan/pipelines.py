# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class DongguanPipeline:
    File=open('donguan.json','w')
    def process_item(self, item, spider):
        content=json.dumps(item,ensure_ascii=False)
        self.File.write(content)
        return item
