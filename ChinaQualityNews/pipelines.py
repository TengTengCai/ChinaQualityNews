# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from pymysql import Error as DBError

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
        self.add_content(item)
        return item

    def add_content(self, item):
        title = item.get('title', '')
        publish_time = item.get('publish_time', '')
        info_sources = item.get('info_sources', '')
        company_name = item.get('company_name', '')
        company_address = item.get('company_address', '')
        sampled_unit = item.get('sampled_unit', '')
        sampled_address = item.get('sampled_address', '')
        sample_name = item.get('sample_name', '')
        specification_type = item.get('specification_type', '')
        trademark = item.get('trademark', '')
        production_date = item.get('production_date', '')
        factory_num = item.get('factory_num', '')
        approval_num = item.get('approval_num', '')
        unqualified = item.get('unqualified', '')
        test_value = item.get('test_value', '')
        standard = item.get('standard', '')
        sampling_unit = item.get('sampling_unit', '')
        inspection_institution = item.get('inspection_institution', '')
        source_url = item.get('source_url', '')

        sql = "INSERT INTO unqualified_sampling (" \
              "title, publish_time, info_sources, company_name, company_address, " \
              "sampled_unit, sampled_address, sample_name, specification_type, trademark, " \
              "production_date, factory_num, approval_num, unqualified, test_value, " \
              "standard, sampling_unit, inspection_institution, " \
              "source_url) values ('{title}', '{publish_time}', '{info_sources}', '{company_name}', '{company_address}', " \
              "'{sampled_unit}', '{sampled_address}', '{sample_name}', '{specification_type}', '{trademark}', " \
              "'{production_date}', '{factory_num}', '{approval_num}', '{unqualified}', '{test_value}', " \
              "'{standard}', '{sampling_unit}', '{inspection_institution}', '{source_url}');".\
            format(title=title, publish_time=publish_time, info_sources=info_sources, company_name=company_name, company_address=company_address,
                   sampled_unit=sampled_unit, sampled_address=sampled_address, sample_name=sample_name, specification_type=specification_type, trademark=trademark,
                   production_date=production_date, factory_num=factory_num, approval_num=approval_num,unqualified=unqualified, test_value=test_value,
                   standard=standard, sampling_unit=sampling_unit, inspection_institution=inspection_institution, source_url=source_url)
        sql.replace("\\", '/')
        print(sql)
        print("Do Insert ...")
        try:
            self.db.ping(reconnect=True)
            with self.db.cursor() as cursor:
                cursor.execute(sql)
            self.db.commit()
            print("Insert Success...")
        except DBError as e:
            # print(e)
            raise e