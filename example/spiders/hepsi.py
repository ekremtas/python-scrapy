import scrapy
from ..items import HepsiItem
from scrapy import Request
from urllib.parse import urljoin
from urllib.parse import urlparse


class HepsiSpider(scrapy.Spider):
    name = 'hepsi'
    start_urls = ["https://www.hepsiburada.com/iphone-ios-telefonlar-c-60005202",
                  "https://www.hepsiburada.com/iphone-ios-telefonlar-c-60005202?sayfa=2"]

    def parse(self, response):
        for href in response.css('div.box.product a::attr(href)').getall():
            top = "https://www.hepsiburada.com/"
            end = "-yorumlari"
            for x in range(1, 10):
                page = ("?sayfa%d" % (x))
                url = ("%s%s%s%s" % (top, href, end, page))
                yield scrapy.Request(url, callback=self.parse_commentpage)
            yield
        yield

    def parse_commentpage(self, response):
        item = HepsiItem()

        print("-------------------------------")
        product_name = response.css('div.productRateBox-2Zcn0 span::text').get()
        print("-------------------------------")
        print("++++++++++++++++++++++++++++++++++++++++")
        product_allcomment = response.css('div.ReviewCard-14zxO').css('div.ReviewCard-3LdJx span::text').getall()
        product_title = response.css('div.ReviewCard-3LdJx strong::text').getall()
        product_date = response.css('div.ReviewCard-1tqv3 *::text').getall()
        for x in range(0, 20):

            item["product_name"] = product_name
            item["product_allcomment"] = product_allcomment[x]
            item["product_title"] =product_title[x]
            item["product_date"] =product_date[x]

            yield item
        yield        

