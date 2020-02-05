# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CfProCrawlerItem(scrapy.Item):
    product_code = scrapy.Field()
    product_name = scrapy.Field()
    product_brand = scrapy.Field()
    product_price = scrapy.Field()
    product_desc = scrapy.Field()
    product_url = scrapy.Field()

    image_urls = scrapy.Field()
    images = scrapy.Field()
