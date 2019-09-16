# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 去重过滤器
import json
import pymysql
#from scrapy import log

from project1.items import BlogItem

class Project1Pipeline(object):
    def process_item(self, item, spider):
        return item

class DuplicatesPipeline(object):
    def __init__(self):
        self.id_set = set()   #内部使用一个 set() 维护数据

    def process_item(self, item, spider):
        if item['user_id'] not in self.id_set:
            self.id_set.add(item['user_id'])
            return item

# 格式化输出 Json (将每一个 item 都输出为一个 json 字符串)
class JsonWritePipeline(object):
    def __init__(self):
        self.output = open('json_format.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + "\n"
        self.output.write(line)
        return item

    def close_spider(self):
        self.output.close()

# 格式化输出为CSV文件
class CSVWritePipeline(object):
    def __init__(self):
        self.output = open('data.csv', 'w', encoding='utf-8')
        self.output.write('user_id,user_name,visit_count,rank'+"\n")

    def process_item(self, item, spider):
        line = self.__checkout(item['user_id']) + ',' + self.__checkout(item['user_name']) + ',' \
            + self.__checkout(item['visit_count']) + ',' + self.__checkout(item['rank'])
        self.output.write(line)
        return item

    def __checkout(self, src_str):
        for ch in str(src_str):
            if ch == ' ' or ch == ',':
                return '"' + src_str + '"'
        return src_str

    def close_spider(self):
        self.output.close()

# 储存到 MySQL 数据库( 使用 pymysql 模块)：不考虑优化，直接实现功能
class MySQLPipeline(object):

    # 启动 spider 时，创建数据库连接对象
    def open_spider(self):
        host = "localhost"
        user = "root"
        password = "23333"
        db_name = "CSDNDB"
        try:
            self.db = pymysql.connect(host,user,password,db_name)
        except:
            log.msg("mysql connection error", level=log.ERROR)


    def process_item(self, item, spider):
        cursor = self.db.cursor()
        sql = "INSERT INTO CSDNDB(user_id,user_name,visit_count,rank) VALUES(%s,%s,%d,%d) " % \
              (item['user_id'], item['user_name'], item['visit_count'], item['rank'])
        try:
            cursor.execute(sql)
            self.db.commit()
        except:
            self.db.rollback()
        return item

    # 关闭 spider 时，销毁数据库连接对象
    def close_spider(self):
        self.db.close()
