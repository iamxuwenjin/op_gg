# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from op_gg.items import PickItem,BanItem


class BanPickSpider(scrapy.Spider):
    name = 'ban_pick'
    allowed_domains = ['op.gg']
    # start_urls = ['http://op.gg/']
    chart_type = ['picked',"banned"]
    def start_requests(self):
        url = "http://www.op.gg/statistics/ajax2/champion/"
        formdata = {"type":"",
                    "league":"",
                    "period":"month",
                    "mapId":"1",
                    "queue":"ranked"}
        for type in self.chart_type:
            formdata['type'] = type
            if formdata['type'] == "picked":
                yield scrapy.FormRequest(url=url, formdata=formdata, callback=self.pick_parse)
            else:
                yield scrapy.FormRequest(url=url, formdata=formdata, callback=self.ban_parse)

    def parse(self, response):
        soup = BeautifulSoup(response.body, "lxml")
        info_list = soup.select('tbody[class="Content"] tr')
        return info_list

    def pick_parse(self, response):
        info_list  = self.parse(response)
        for info in info_list:
            item = PickItem()
            item['rank'] = info.select('td')[0].get_text()
            item['hero'] = info.select('td')[2].get_text().strip()
            item['pick_rate'] = info.select('td')[3].get_text().strip()
            yield item

    def ban_parse(self,response):
        info_list = self.parse(response)
        for info in info_list:
            item = BanItem()
            item['rank'] = info.select('td')[0].get_text()
            item['hero'] = info.select('td')[2].get_text().strip()
            item['ban_rate'] = info.select('td')[3].get_text().strip()
            yield item