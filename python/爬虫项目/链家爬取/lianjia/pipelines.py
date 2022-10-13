# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
import pymysql

class LianjiaPipeline:
    def open_spider(self,spider):
        self.client = pymongo.MongoClient()

    def process_item(self, item, spider):
        # self.client.lianjia.ershoufang.insert()
        # keys = item['keys']
        # values = item['values']

        self.client.lianjia.ershoufang.insert(item)
        return item

    def close_spider(self,spider):
        self.client.close()

class MysqlPipeline(object):
    # 执行前数据库中需要有对应的表

    def open_spider(self,spider):
        self.client = pymysql.connect(host="",port="",user="",password="",db="",charset="")
        self.cursor = self.client.cursor()

    def process_item(self,item,spider):
        # 按照传过来的属性需要修改下面的sql
        args=[item["key1"],item["key2"]]
        sql='insert into 表明 values(%s,%s)'
        self.cursor.execute(sql,args)
        self.client.commit()

    def close_spider(self,spider):
        self.cursor.close()
        self.client.close()