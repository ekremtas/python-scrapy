import scrapy
from ..items import TeknoItem
from scrapy import Request
from urllib.parse import urljoin
from urllib.parse import urlparse

class TeknoSpider(scrapy.Spider):
    name = 'tekno'
    start_urls = ["https://www.teknosa.com/apple-iphone-6-32-gb-gold-akilli-telefon-p-125076759"]
    
    def parse(self, response):
        item = TeknoItem()

        product_name = response.css('.product-title').css('h1::text').extract()
        print("--------product-name-------")
        print(product_name)
        print("--------product-name-------")
        product_allcomment = response.css('div.comment-item *::text').getall()

        product_brand = response.css('.brand-name').css('::text').extract()

        product_numbercomment = response.css(
            '#comments-container').css('::text').getall()

        item["product_name"] = product_name
        item["product_allcomment"] = product_allcomment
        item["product_brand"] = product_brand
        item["product_numbercomment"] = product_numbercomment

        print("--------product-brand-------")
        print(product_brand)
        print("-------product-brand--------")

        yield item
