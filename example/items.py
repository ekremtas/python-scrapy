# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


# class ExampleItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     product_name = scrapy.Field()
#     product_allcomment = scrapy.Field()
#     product_brand = scrapy.Field()
#     product_price = scrapy.Field()
#     product_numbercomment = scrapy.Field()
#     product_star = scrapy.Field()
#     product_comments = scrapy.Field()
#     pass

class ExampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name = scrapy.Field()
    product_allcomment = scrapy.Field()
    product_brand = scrapy.Field()
    product_price = scrapy.Field()
    product_numbercomment = scrapy.Field()
    product_star = scrapy.Field()
    product_comments = scrapy.Field()



    pass
class TeknosaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    final_image = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    stars = scrapy.Field()
    description = scrapy.Field()
    upc = scrapy.Field()
    price_excl_tax = scrapy.Field()
    price_inc_tax = scrapy.Field()
    tax = scrapy.Field()



    pass

class HepsiItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name = scrapy.Field()
    product_allcomment = scrapy.Field()
    product_title = scrapy.Field()
    product_date = scrapy.Field()



    pass

class TeknoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    product_name = scrapy.Field()
    product_brand = scrapy.Field()
    product_numbercomment = scrapy.Field()
    product_allcomment = scrapy.Field()



    pass