import scrapy
from ..items import ExampleItem
from scrapy import Request
from urllib.parse import urljoin
from urllib.parse import urlparse


class Example2Spider(scrapy.Spider):
    name='example2'
    start_urls=["https://www.hepsiburada.com/cep-telefonlari-c-371965?sayfa=3"]

    def parse(self,response):
        for x in range(1,25):
            for href in response.xpath("/html/body/div[3]/main/div[4]/div/div/div/div[2]/section/div[8]/div[3]/div/div/div/div/ul/li[%d]/div/a/@href"% (x)):
                url = response.urljoin(href.extract())
                print("------------------------\n\n")
                print(url)
                
                print("\n\n------------------------")
                yield scrapy.Request(url, callback=self.parse_page)
        
        

    def parse_page(self,response):
        item = ExampleItem()
        #product_name = response.xpath("/html/body/div[4]/main/div[3]/section[1]/div[4]/div/div[4]/div[1]/header/h1/text()").extract()
        product_name = response.css('#product-name').css('::text').extract()

        print("--------product-name-------")
        print(product_name)
        print("--------product-name-------")
        #product_allyorum = response.xpath("/html/body/div[4]/main/div[3]/section[3]/div/div/div[2]/div/div[2]/div[1]/ul/span/a/@href").extract()
        product_allyorum = response.css('.button-more-results::attr(href)').extract()

        print("--------product-yorumlink-------")
        print(product_allyorum)
        print("-------product-yorumlink--------")
        item["product_name"]=product_name
        item["product_allyorum"]=product_allyorum
        print("--------product-name-------")
        print(product_name)
        print("--------product-name-------")
        print("--------product-yorumlink-------")
        print(product_allyorum)
        print("-------product-yorumlink--------")
        hp_link = "https://www.hepsiburada.com"
        asd =("%s%s"% (hp_link,product_allyorum[0]))
        print(asd)
        #for href in response.xpath("%s%s"% (hp_link,product_allyorum[0])):
        #    url = response.urljoin(href.extract())
        #    print("------------------------\n\n")
        #    print(url)
        #    
        #    print("\n\n------------------------")
        #    yield scrapy.Request(url, callback=self.parse_yorumpage)



        yield item

    #def parse_yorumpage(self,response):
     #   item = ExampleItem()
      #  #product_name = response.xpath("/html/body/div[4]/main/div[3]/section[1]/div[4]/div/div[4]/div[1]/header/h1/text()").extract()
       # product_allyorumlarr = response.css('#product-name').css('::text').extract()
     #   print("--------product-name-------")
      #  print(product_allyorumlarr)
       # print("--------product-name-------")

        #item["product_allyorumlarr"]=product_allyorumlarr


        #yield item.product_allyorumlarr
        


