# email_extractor/spiders/email_spider.py

import scrapy
from ..items import EmailExtractorItem

class EmailSpider(scrapy.Spider):
    name = 'email_spider'
    start_urls = ['https://www.example.com']

    def parse(self, response):
        items = []
        for selector in response.css('your_selector_for_usernames_and_passwords'):
            item = EmailExtractorItem()
            item['username'] = selector.css('your_username_selector::text').get()
            item['password'] = selector.css('your_password_selector::text').get()
            items.append(item)
        return items
