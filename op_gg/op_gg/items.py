# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HeroItem(scrapy.Item):
    rank = scrapy.Field()
    hero = scrapy.Field()
    win_rate = scrapy.Field()
    count = scrapy.Field()
    KDA = scrapy.Field()
    CS = scrapy.Field()
    money = scrapy.Field()
    type = scrapy.Field()
    queue = scrapy.Field()
    source = scrapy.Field()
    # utc时间
    utc_time = scrapy.Field()

class BanItem(scrapy.Item):
    source = scrapy.Field()
    utc_time = scrapy.Field()
    hero = scrapy.Field()
    ban_rate = scrapy.Field()
    rank = scrapy.Field()

class PickItem(scrapy.Item):
    source = scrapy.Field()
    # utc时间
    utc_time = scrapy.Field()
    hero = scrapy.Field()
    pick_rate = scrapy.Field()
    rank = scrapy.Field()

class PlayerItem(scrapy.Item):
    source = scrapy.Field()
    utc_time = scrapy.Field()
    rank = scrapy.Field()
    player = scrapy.Field()
    rank_info = scrapy.Field()
    LP = scrapy.Field()
    team = scrapy.Field()
    win_rate = scrapy.Field()
