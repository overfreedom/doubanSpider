# -*- coding: utf-8 -*-
import scrapy
from time import sleep
import re
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DoubanspiderItem


class BookDoubanSpSpider(CrawlSpider):
    name = 'book_douban_sp'
    allowed_domains = ['book.douban.com']
    tag = ['程序', '编程', '算法']
    start_urls  = ['https://book.douban.com/tag/' + i for i in tag]
    # start_urls = ['https://book.douban.com/tag/程序',
    #               'https://book.douban.com/tag/编程',
    #               'https://book.douban.com/tag/算法',]

    pl_re = re.compile(r'(\d+)人')

    rules = (
        Rule(LinkExtractor(
            allow=r'\?start=\d+\&type=T'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(
        #     allow=r'\?start=\d+\&type=T'), callback='parse_item', follow=True),
        # Rule(LinkExtractor(
        #     allow=r'\?start=\d+\&type=T'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):               
        responselist = response.xpath('//li[@class="subject-item"]')
        for li in responselist:
            item = DoubanspiderItem()
            item['url'] = li.xpath('div[@class="info"]//a/@href').get()
            item['title'] = li.xpath('div[@class="info"]//a/@title').get()
            if(li.xpath('div[@class="info"]//a/span')):
                item['sub_title'] = li.xpath(
                    'div[@class="info"]//a/span/text()').get()
            item['score'] = li.xpath(
                'div//span[@class="rating_nums"]/text()').get()
            pl = li.xpath('div//span[@class="pl"]/text()').get()
             
            item['people_counting'] = self.pl_re.findall(pl)[0]
            # print(item)
            yield item
