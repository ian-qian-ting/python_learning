#!/usr/bin/python

# File Usage: Web Crawler demo
# Last Edit: 2019/09/03
# Author: Ian Qian Ting

#import scrapy module
import scrapy

class BrickSetSpider(scrapy.Spider):
  name = "brickset_spider"
  start_urls = ['http://brickset.com/sets/year-2016']

  def parse(self, response):
    SET_SELECTOR = '.set'
    for brickset in response.css(SET_SELECTOR):
      NAME_SELECTOR = 'h1 ::text'
      yield {
        'name':brickset.css(NAME_SELECTOR).extract_first(),
      }
