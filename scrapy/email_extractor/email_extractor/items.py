# email_extractor/items.py

import scrapy

class EmailExtractorItem(scrapy.Item):
    name = scrapy.Field()
    email = scrapy.Field()
    username = scrapy.Field()
    password = scrapy.Field()
