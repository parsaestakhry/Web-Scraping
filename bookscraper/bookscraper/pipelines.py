# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        
        #strip all the whitespaces from strings
        field_names = adapter.field_names()
        for field_name in field_names:
            if field_names != 'description':
                value = adapter.get(field_name)
                adapter[field_name] = value.strip()
        return item
