# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CqnSpider(CrawlSpider):
    name = 'cqn'
    allowed_domains = ['www.cqn.com.cn']
    start_urls = ['http://www.cqn.com.cn/']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.cqn.com.cn/ms/content/\d+-\d+/\d+/content_\d+.htm'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        news_type = response.xpath('./body//div[@class="box"][1]//a[4]/text()').extract_first()
        if news_type == '国家抽查':
            item['title'] = response.xpath()
            item['publish_time'] = response.xpath()
            item['info_sources'] = response.xpath()
            item['company_name'] = response.xpath()
            item['company_address'] = response.xpath()
            item['sampling_unit'] = response.xpath()
            item['sampling_address'] = response.xpath()
            item['sample_name'] = response.xpath()
            item['specification_type'] = response.xpath()
            item['trademark'] = response.xpath()
            item['unqualified'] = response.xpath()
            item['test_value'] = response.xpath()
            item['standard'] = response.xpath()
            item['inspection_institution'] = response.xpath()
        return item
