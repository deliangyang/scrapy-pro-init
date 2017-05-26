# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider

class BlogCsdnSpider(RedisSpider):
    name = "blog_csdn"
    allowed_domains = ["blog.csdn.net"]
    #start_urls = ['http://blog.csdn.net/']

    def parse(self, response):
        for title in response.xpath('//title/text()').extract():
            print title
