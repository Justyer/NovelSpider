# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NovelItem(scrapy.Item):
    name      = scrapy.Field()
    win_rate  = scrapy.Field()
    pick_rate = scrapy.Field()
    ban_rate  = scrapy.Field()
