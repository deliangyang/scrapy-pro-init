# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from scrapy_pro_init.items import ScrapyProInitItem

class BlogCsdnSpider(RedisSpider):
    name = "blog_csdn"
    allowed_domains = [
        "blog.csdn.net",
        "c.csdnimg.cn"
    ]
    #start_urls = ['http://blog.csdn.net/']

    def parse(self, response):
        item = ScrapyProInitItem()
        item['image_urls'] = []
        for image in response.xpath('//img/@src').extract():
            print image
            item['image_urls'].append(image)
        yield item
        # for title in response.xpath('//title/text()').extract():
        #     print title


