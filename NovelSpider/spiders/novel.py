# -*- coding: utf-8 -*-

from scrapy.http import Request
from scrapy.selector import Selector
from NovelSpider.scrapy_redis.spiders import RedisCrawlSpider
from NovelSpider.items import NovelItem

class NovelSpider(RedisCrawlSpider):
    name = "novel"
    redis_key = 'novel:start_urls'

    def __init__(self, *args, **kwargs):
        # Dynamically define the allowed domains list.
        super(NovelSpider, self).__init__(*args, **kwargs)

    def parse(self, response):
        li = Selector(response).xpath('//*[@class="row"]').extract()
        item = NovelItem()
        for i in li:
            iv = Selector(text=i)
            item['name']        = iv.xpath('//*[@class="item2"]/span[2]/text()').extract_first()
            item['win_rate']    = iv.xpath('//div[@class="item3"][1]/div/span/@data-val').extract_first()
            item['pick_rate']   = iv.xpath('//div[@class="item3"][2]/div/span/@data-val').extract_first()
            item['ban_rate']    = iv.xpath('//div[@class="item3"][3]/div/span/@data-val').extract_first()
            yield item
