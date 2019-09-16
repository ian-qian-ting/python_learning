# -*- coding: utf-8 -*-
import scrapy
#from scrapy import log
from project1.items import BlogItem

class Spider1Spider(scrapy.Spider):
    name = 'spider1'
    allowed_domains = ['my.csdn.net', 'blog.csdn.net']
    start_urls = ['http://my.csdn.net/al_assad']

# access user page to collect user list
    def parse(self, response):
#        pass
        blog_page_url = 'http://blog.csdn.net/' + response.url.split('/')[-1]
        scrapy.http.Request(blog_page_url, self.blog_parse)
        user_list = response.xpath('//div[@class="header clearfix"]/a/@href').extract()
        for user_name in user_list:
            user_page_url = 'http://my.csdn.net/'+user_name
            yield scrapy.http.Request(user_page_url, self.parse)

# access user blog page to collect user data
    def blog_parse(self, response):
        blog_item = BlogItem()

        if response.xpath('//ul[@class="panel_body profile"]'): #old version
            blog_item['user_id'] = response.url.split('/')[-1]
            blog_item['user_name'] = response.xpath('//a[@class="user_name"]/text()').extract()[0]
            blog_item['visit_count'] = response.xpath('//ul[@id="blog_rank"]/li[1]/span/text()').extract()[0][:-1]
            blog_item['rank'] = response.xpath('//ul[@id="blog_rank"]/li[1]/span/text()').extract()[0][1:-1]
        else:
            blog_item['user_id'] = response.url.split('/')[-1]
            blog_item['user_name'] = response.xpath('//a[@id="uid"]/text()').extract()[0]
            blog_item['visit_count'] = ''.join(response.xpath('//div[@class="gradeAndbadge"][1]/span[@class="num"]/text()').extract()[0].split(','))
            blog_item['rank'] = response.xpath('//div[@class="gradeAndbadge"][3]/span[@class="num"]/text()').extract()[0]

        log.msg(blog_item, level=log.INFO)
        yield blog_item
