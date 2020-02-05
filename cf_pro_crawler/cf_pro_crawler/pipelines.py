# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import os


class CfProCrawlerPipeline(object):
    def process_item(self, item, spider):
        os.chdir('/home/zx/Desktop/cf-pro-crawler-app/cf_pro_crawler/product_images')

        for num in range(len(item['images'])): 
            if item['images'][num]['path']:
            	new_image_name = item['product_code'][0] + '_{}.jpg'.format(num+1)
            	new_image_path = 'full/' + new_image_name

            	os.rename(item['images'][num]['path'], new_image_path)