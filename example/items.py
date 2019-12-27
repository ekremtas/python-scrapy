# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ExampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name = scrapy.Field()
    product_allcomment = scrapy.Field()
    product_brand = scrapy.Field()
    product_price = scrapy.Field()
    product_numbercomment = scrapy.Field()
    product_star = scrapy.Field()
    pass
