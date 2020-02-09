# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from collections import defaultdict


class CfProCrawlerItem(scrapy.Item):
    fields = defaultdict(scrapy.Field)
    images = scrapy.Field()

    def __setitem__(self, key, value):
        # all keys are supported
        self._values[key] = value
        