# -*- coding: utf-8 -*-
import scrapy


class ProductSpider(scrapy.Spider):
    name = 'product'
    allowed_domains = ['www.carrefoursa.com/tr/']
    start_urls = ['https://www.carrefoursa.com/tr/pinar-ac-bitir-buyuk-dilim-hindi-salam-60-g-p-30202211']

    # def __init__(self, *args, **kwargs):
    #     super(ProductSpider, self).__init__(*args, **kwargs)
    #     self.start_urls = kwargs.get('start_urls').split(',')

    def parse(self, response):
    	product_code = response.xpath('//*[@id="addToCartForm"]/input[3]/@value').extract_first()
        
        product_name = response.xpath('//*[@class="product-details"]/div[@class="name"]/h1/text()').extract_first()
        
        product_brand = response.xpath('//*[@class="product-details"]/div[@class="brand"]/span/a/text()').extract_first()
        product_brand = product_brand.strip()
        
        product_price = response.xpath('//span[contains(@class, "item-price")]/text()').extract_first()
        
        product_desc = response.xpath('//*[@class="col-xs-12 col-sm-12"]//text()').extract()
        product_desc = ' \n'.join([i.strip() for i in product_desc])
        
        product_cats = response.xpath('//*[@class="breadcrumb"]//a').extract()
        product_cats = [cat.split('>') for cat in product_cats[1:]]
        product_cat_nums = [cat_num[0].split('/')[-1].split('"')[0] for cat_num in product_cats]
        product_cat_names = [cat_name[1].split('<')[0] for cat_name in product_cats]

        yield{
            'product_code': product_code,
			'product_name': product_name,
			'product_brand': product_brand,
			'product_price': product_price,
			'product_desc': product_desc,
			yield{('product_cat_num'+'{}'.format(i) for i in range(len(product_cat_nums))): (product_cat_nums[num] for num in range(len(product_cat_nums)))}
			# 'product_cats': product_cats,
			# 'product_cat_nums': product_cat_nums,
			# 'product_cat_names': product_cat_names
		}

        # for num in range(len(product_cat_nums)):
        #  	yield{
        #  		'product_cat_num' + "{}".format(num+1): product_cat_nums[num]
        #  	}

    def parseCats(self, response):
    	