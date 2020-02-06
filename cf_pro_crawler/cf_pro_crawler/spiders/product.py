# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from cf_pro_crawler.items import CfProCrawlerItem
import re


class ProductSpider(scrapy.Spider):
    name = 'product'
    allowed_domains = ['www.carrefoursa.com/tr/']
    # start_urls = ['https://www.carrefoursa.com/tr/lg-55sm8000pla-nanocell-4k-ultra-hd-55-140-ekran-uydu-alicili-smart-led-televizyon-p-30262223']

    def __init__(self, *args, **kwargs):
        super(ProductSpider, self).__init__(*args, **kwargs)
        self.start_urls = kwargs.get('start_urls').split(',')

    def parse(self, response):
        product_code = response.xpath('//*[@id="addToCartForm"]/input[3]/@value').extract_first()

        product_name = response.xpath('//*[@class="product-details"]/div[@class="name"]/h1/text()').extract_first()

        product_brand = response.xpath('//*[@class="product-details"]/div[@class="brand"]/span/a/text()').extract_first()
        product_brand = product_brand.strip()

        product_price = response.xpath('//span[contains(@class, "item-price")]/text()').extract_first()

        product_desc = response.xpath('//*[@class="col-xs-12 col-sm-12"]//text()').extract()
        product_desc = '\n'.join([i.strip() for i in product_desc])

        product_url = response.url

        bodyRes = response.body.decode('utf-8')
        image_urls = re.findall('https://reimg-carrefour.mncdn.com/mnresize/600/600/productimage/?\/.*\.(?:jpg)+', bodyRes)
        image_urls = list(set(image_urls))

        product_cats = response.xpath('//*[@class="breadcrumb"]//a').extract()
        product_cats = [cat.split('>') for cat in product_cats[1:]]
        product_cat_nums = [cat_num[0].split('/')[-1].split('"')[0] for cat_num in product_cats]
        product_cat_names = [cat_name[1].split('<')[0] for cat_name in product_cats]

        l = ItemLoader(item=CfProCrawlerItem(), response=response)

        l.add_value('product_code', product_code)
        l.add_value('product_name', product_name)
        l.add_value('product_brand', product_brand)
        l.add_value('product_price', product_price)
        l.add_value('product_desc', product_desc)
        l.add_value('product_url', product_url)
        l.add_value('image_urls', image_urls)
        l.add_value('product_cat_nums', product_cat_nums)
        l.add_value('product_cat_names', product_cat_names)

        return l.load_item()
