# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from ChinaQualityNews.items import ChinaqualitynewsItem


class CqnSpider(CrawlSpider):
    name = 'cqn'
    allowed_domains = ['www.cqn.com.cn']
    start_urls = ['http://www.cqn.com.cn/ms/node_20334.htm']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.cqn.com.cn/ms/content/2019-\d+/\d+/content_\d+.htm'),
             callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        # item['name'] = response.xpath('//div[@id="name"]').get()
        # item['description'] = response.xpath('//div[@id="description"]').get()
        news_type = response.xpath('./body//div[@class="box"][1]//a[4]/text()').extract_first()
        if news_type is None:
            return
        news_type = news_type.strip()
        year = response.xpath('./body//div[@class="box"][1]//a[5]/text()').extract_first()
        if year is None:
            return
        year = year.strip()
        if news_type == '国家抽查' and year == '2019':
            big_title = response.xpath('.//div[@class="Detail_Title"]/h1/text()').extract_first().strip().split('：')
            if len(big_title) >= 2:
                title = ''.join(big_title[1:])
                info_sources = big_title[0]
            else:
                title = ''.join(big_title)
                info_sources = ''
            publish_time = response.xpath('.//div[@class="publish"][1]/text()').extract_first().strip()

            tables = response.xpath('.//table[@class="MsoNormalTable"]')
            if len(tables) == 0:
                tables = response.xpath('.//table[@style]')
                if len(tables) == 0:
                    tables = response.xpath('.//table')
            for table in tables:
                trs = table.xpath('.//tr')
                temp = []
                tr = trs[0]
                tds = tr.xpath('.//td')
                if len(tds) == 1:
                    col_num = tds[0].xpath('.//@colspan').extract_first()
                    col_num = 1 if col_num is None else int(col_num)
                    trs.pop(0)
                    trs.pop(0)
                else:
                    col_num = len(tds)
                    for td in tds:
                        if '备注' == td.xpath('.//span//text()').extract_first():
                            col_num -= 1
                    trs.pop(0)

                for tr in trs:
                    item = ChinaqualitynewsItem()
                    item['title'] = title
                    item['info_sources'] = info_sources
                    item['publish_time'] = publish_time
                    item['source_url'] = response.url
                    tds = tr.xpath('.//td')
                    index = 0
                    if len(tds) < col_num:
                        for i in temp:
                            if i is None:
                                td = tds.pop(0)
                                value = ''.join(td.xpath('.//span//text()').extract())
                            else:
                                value = i
                            item = self.table_col_adapter(col_num, item, index, value)
                            index += 1
                        yield item
                    else:
                        temp = []
                        for td in tds:
                            value = ''.join(td.xpath('.//span//text()').extract())
                            item = self.table_col_adapter(col_num, item, index, value)
                            row = td.xpath('./@rowspan').extract_first()
                            if row is not None:
                                temp.append(value)
                            else:
                                temp.append(None)
                            index += 1
                        yield item

    @staticmethod
    def create_item_to_9(item, index, value):
        if index == 0:
            return item
        elif index == 1:
            item['sample_name'] = value
        elif index == 2:
            item['sampled_unit'] = value
        elif index == 3:
            item['company_name'] = value
        elif index == 4:
            item['specification_type'] = value
        elif index == 5:
            item['factory_num'] = value
        elif index == 6:
            item['sample_name'] = value
        elif index == 7:
            item['inspection_institution'] = value
        elif index == 8:
            item['unqualified'] = value
        return item


    @staticmethod
    def create_item_to_11(item, index, value):
        if index == 0:
            return item
        elif index == 1:
            item['company_name'] = value
        elif index == 2:
            item['company_address'] = value
        elif index == 3:
            item['sampled_unit'] = value
        elif index == 4:
            item['sampled_address'] = value
        elif index == 5:
            item['sample_name'] = value
        elif index == 6:
            item['specification_type'] = value
        elif index == 7:
            item['trademark'] = value
        elif index == 8:
            item['production_date'] = value
        elif index == 9:
            item['unqualified'] = value
        elif index == 10:
            item['test_value'] = value
        return item

    @staticmethod
    def create_item_to_12(item, index, value):
        if index == 0:
            return item
        elif index == 1:
            item['company_name'] = value
        elif index == 2:
            item['company_address'] = value
        elif index == 3:
            item['sampled_unit'] = value
        elif index == 4:
            item['sampled_address'] = value
        elif index == 5:
            item['sample_name'] = value
        elif index == 6:
            item['specification_type'] = value
        elif index == 7:
            item['trademark'] = value
        elif index == 8:
            item['unqualified'] = value
        elif index == 9:
            item['test_value'] = value
        elif index == 10:
            item['standard'] = value
        elif index == 11:
            item['inspection_institution'] = value
        return item

    @staticmethod
    def create_item_to_13(item, index, value):
        if index == 0:
            return item
        elif index == 1:
            item['company_name'] = value
        elif index == 2:
            item['company_address'] = value
        elif index == 3:
            item['sampled_unit'] = value
        elif index == 4:
            item['sampled_address'] = value
        elif index == 5:
            item['sample_name'] = value
        elif index == 6:
            item['specification_type'] = value
        elif index == 7:
            item['trademark'] = value
        elif index == 8:
            item['production_date'] = value
        elif index == 9:
            item['unqualified'] = value
        elif index == 10:
            item['test_value'] = value
        elif index == 11:
            item['standard'] = value
        elif index == 12:
            item['inspection_institution'] = value
        return item

    @staticmethod
    def create_item_to_14(item, index, value):
        if index == 0:
            return item
        elif index == 1:
            item['company_name'] = value
        elif index == 2:
            item['company_address'] = value
        elif index == 3:
            item['sampled_unit'] = value
        elif index == 4:
            item['sampled_address'] = value
        elif index == 5:
            item['sample_name'] = value
        elif index == 6:
            item['approval_num'] = value
        elif index == 7:
            item['trademark'] = value
        elif index == 8:
            item['factory_num'] = value
        elif index == 9:
            item['production_date'] = value
        elif index == 10:
            item['specification_type'] = value
        elif index == 11:
            item['unqualified'] = value
        elif index == 12:
            item['test_value'] = value
        elif index == 13:
            item['standard'] = value
        elif index == 14:
            item['inspection_institution'] = value
        return item

    def table_col_adapter(self, items_len, item, index, value):
        if items_len == 9:
            item = self.create_item_to_9(item, index, value)
        elif items_len == 11:
            item = self.create_item_to_11(item, index, value)
        elif items_len == 12:
            item = self.create_item_to_12(item, index, value)
        elif items_len == 13:
            item = self.create_item_to_13(item, index, value)
        elif items_len == 14:
            item = self.create_item_to_14(item, index, value)
        return item
