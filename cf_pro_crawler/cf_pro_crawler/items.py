# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
#from cf_pro_crawler.product import ProductSpider


class CfProCrawlerItem(scrapy.Item):
    product_code = scrapy.Field()
    product_name = scrapy.Field()
    product_brand = scrapy.Field()
    product_price = scrapy.Field()
    product_desc = scrapy.Field()
    product_url = scrapy.Field()
    product_cat_nums = scrapy.Field()
    product_cat_names = scrapy.Field()

    image_urls = scrapy.Field()
    images = scrapy.Field()

