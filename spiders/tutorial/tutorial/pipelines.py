# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

## 数据处理，处理后,可以入库，可以写入文件,需要在setting.py中进行配置

class TutorialPipeline:
    def process_item(self, item, spider):
        print('---------------------')
        return item
