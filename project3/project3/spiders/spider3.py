# -*- coding: utf-8 -*-

# Usage: Create a spider to collect tap tap information
# Author: Ian Qian Ting
# Last Edit: 2019/09/11

import scrapy
import urllib
import json
from datetime import datetime


class Spider3Spider(scrapy.Spider):
    name = 'spider3'
    allowed_domains = ['taptap.com']
    start_urls = ['https://www.taptap.com/auth/email/login']
    url_lists = ['https://www.taptap.com/169944/review']

    params = {
        'email':'641729094@qq.com',
        'password':'QTtest27'
    }

    # hd = {'User-Agent':user_agent}
        
    def parse(self, response):
        # pass
        return scrapy.FormRequest.from_response(response, formdata=params, callback=self.after_login)

    def after_login(self, response):
        if authentication_failed(response):
            self.logger.error("Login failed!")
        else:
            print("Login Success")
        #continue scraping with authenticated session
        #for url in url_lists:
        #    yield scrapy.Request(url=url, callback=self.save_parse)

    def save_parse(self, response):
        filename = 'review_' + datetime.now().time().strftime('%H:%M:%S')
        with open(filename,'wb') as f:
            f.write(response.body)
        self.log('saved file %s' % filename)

