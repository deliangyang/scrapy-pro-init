# -*- coding: utf-8 -*-
import scrapy


class HshfyShCnSpider(scrapy.Spider):
    name = "hshfy_sh_cn"
    allowed_domains = ["www.hshfy.sh.cn"]
    start_urls = ['http://www.hshfy.sh.cn/']

    def parse(self, response):
        print response.body
        pass

    def start_requests(self):
        pass


