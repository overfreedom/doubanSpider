# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanspiderItem(scrapy.Item):
    title = scrapy.Field()
    sub_title = scrapy.Field()
    score = scrapy.Field()
    people_counting = scrapy.Field()
    url = scrapy.Field()
    pass
