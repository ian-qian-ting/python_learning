# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BlogItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    user_id = scrapy.Field()
    user_name = scrapy.Field()
    visit_count = scrapy.Field()
    rank = scrapy.Field()
