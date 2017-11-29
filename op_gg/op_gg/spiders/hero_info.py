# -*- coding: utf-8 -*-
import scrapy
import time
from op_gg.items import HeroItem
from bs4 import BeautifulSoup


class HeroInfoSpider(scrapy.Spider):
    name = 'hero_info'
    allowed_domains = ['op.gg']
    chart_type = "win"
    game_mode = ["ranked","normal"]
    def start_requests(self):
        url = 'http://www.op.gg/statistics/ajax2/champion/'
        header = {"Accept-Language": "zh-CN,zh;q=0.9"}
        formdata = {"type": "win",  # 图表类型
                    "league": "",  # 战区
                    "period": "month",  # 时间
                    "mapId": "1",  # 地图
                    "queue": ""}
        meta = {'type':'win',
                'queue':''}
        for mode in self.game_mode:
            meta['queue'] = mode
            formdata["queue"] = mode
            print formdata
            yield scrapy.FormRequest(url=url, formdata=formdata, headers=header, meta=meta, callback=self.parse)


    def parse(self, response):
        soup = BeautifulSoup(response.body, "lxml")
        # info_list = response.xpath('//tbody[@class = "Content"]/tr[@role="row"]')
        info_list = soup.select('tbody[class="Content"] tr')
        print len(info_list)
        for info in info_list:
            item = HeroItem()
            item['rank'] = info.select('td')[0].get_text()
            item['hero'] = info.select('td')[2].get_text().strip()
            item['win_rate'] = info.select('td')[3].get_text().strip()
            item['count'] = info.select('td')[4].get_text().strip()
            item['KDA'] = info.select('td')[5].get_text().strip()
            item['CS'] = info.select('td')[6].get_text().strip()
            item['money'] = info.select('td')[7].get_text().strip()
            item['type'] = response.meta['type']
            item['queue'] = response.meta['queue']
            yield item