# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

from ChinaQualityNews.settings import DB_SETTINGS


class ChinaqualitynewsPipeline(object):
    def __init__(self):
        self._host = DB_SETTINGS.get('host')
        self._port = DB_SETTINGS.get('port')
        self._user = DB_SETTINGS.get('user')
        self._password = DB_SETTINGS.get('password')
        self._db_name = DB_SETTINGS.get('db')
        self.db = pymysql.connect(host=self._host,
                                  user=self._user,
                                  password=self._password,
                                  port=self._port,
                                  db=self._db_name)
        self.db.set_charset('utf8')

    def process_item(self, item, spider):

        return item
