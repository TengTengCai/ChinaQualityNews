# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinaqualitynewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()  # 标题
    publish_time = scrapy.Field()  # 发布时间
    info_sources = scrapy.Field()  # 信息来源
    company_name = scrapy.Field()  # 标称生产企业/进货来源 名称
    company_address = scrapy.Field()  # 标称生产企业/进货来源 地址
    sampled_unit = scrapy.Field()  # 被抽样单位名称
    sampled_address = scrapy.Field()  # 被抽样单位地址
    sample_name = scrapy.Field()  # 样品名称
    specification_type = scrapy.Field()  # 规格型号
    trademark = scrapy.Field()  # 商标
    production_date = scrapy.Field()  # 生产日期
    factory_num = scrapy.Field()  # 出厂编号
    approval_num = scrapy.Field()  # 批准文号
    unqualified = scrapy.Field()  # 不合格项目
    test_value = scrapy.Field()  # 检验结果
    standard = scrapy.Field()  # 标准值
    sampling_unit = scrapy.Field()  # 抽样单位名称
    inspection_institution = scrapy.Field()  # 检验机构
    source_url = scrapy.Field()

    pass
