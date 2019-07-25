# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CqnSpider(CrawlSpider):
    name = 'cqn'
    allowed_domains = ['www.cqn.com.cn']
    start_urls = ['http://www.cqn.com.cn/ms/node_20334.htm']

    rules = (
        Rule(LinkExtractor(allow=r'http://www.cqn.com.cn/ms/content/\d+-\d+/\d+/content_\d+.htm'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        news_type = response.xpath('./body//div[@class="box"][1]//a[4]/text()').extract_first().strip()
        if news_type == '国家抽查':
            big_title = response.xpath('.//div[@class="Detail_Title"]/h1/text()').extract_first().strip().split('：')
            if len(big_title) >= 2:
                title = ''.join(big_title[:1])
                info_sources = big_title[0]
            else:
                title = ''.join(big_title)
                info_sources = ''
            publish_time = response.xpath('.//div[@class="publish"][1]/text()').extract_first().strip()

            tables = response.xpath('.//table[@class="MsoNormalTable"]')
            for table in tables:
                trs = table.xpath('.//tr')
                for tr in trs:
                    tds = tr.xpath('.//td')
                    temp = {}
                    index = 0
                    for td in tds:

                        row = td.xpath('./@rowspan').extract_first()
                        if
                        item['title'] = title
                        item['info_sources'] = info_sources
                        item['publish_time'] = publish_time

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
                        index += 1
                        yield item
