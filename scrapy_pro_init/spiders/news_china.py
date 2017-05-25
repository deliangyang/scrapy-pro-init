# -*- coding: utf-8 -*-
import scrapy
import re


class NewsChinaSpider(scrapy.Spider):
    name = "news_china"
    allowed_domains = ["news.china.com"]
    start_urls = ['http://news.china.com/']

    def is_url(self, url):
        regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        return regex.match(url)

    def parse(self, response):
        for url in response.xpath('//a/@href').extract():
            if (self.is_url(url)):
                print url
                yield scrapy.Request(url, callback=self.xparse)

    def xparse(self, response):
        for title in response.xpath('//title/text()').extract():
            print title
