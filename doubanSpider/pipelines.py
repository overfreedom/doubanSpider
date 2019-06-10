# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymssql

server = 'localhost'
user = 'sa'
password = 'sql'
database = 'doubanbook'
conn = pymssql.connect(server, user, password, database)

cs = conn.cursor()


class DoubanspiderPipeline(object):
    def save_bookinfo(self, item):
        keys = item.keys()
        values = tuple(item.values())
        fields = ','.join(keys)
        tmp = ','.join(['%s'] * len(keys))
        sql = 'insert into bookinfo (%s) values (%s)' % (fields, tmp)
        cs.execute(sql, values)
        return conn.commit()

    def process_item(self, item, spider):
        try:
            self.save_bookinfo(item)
        except Exception as e:
            print(item)
            print(e)
        return item
