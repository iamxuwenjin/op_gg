# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from op_gg.items import PlayerItem


class PlayerInfoSpider(scrapy.Spider):
    name = 'player_info'
    allowed_domains = ['op.gg']
    start_urls = 'http://www.op.gg/ranking/ajax2/ladders/start='
    def start_requests(self):
        num = 0
        while num <= 50:
            url = self.start_urls + str(num)
            print url
            num += 50
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        # with open('ranked.html','w') as f:
        #     f.write(response.body)
        # print response.body
        soup = BeautifulSoup(response.body, "lxml")
        info_list = soup.select('tbody[class="Body"] tr')
        for info in info_list:
            item = PlayerItem()
            item['rank'] = info.select('td')[0].get_text()
            item['player'] = info.select('td')[2].get_text().strip()
            item['rank_info'] = info.select('td')[3].get_text()
            item['LP'] = info.select('td')[4].get_text()
            item['team'] = info.select('td')[5].get_text().strip()
            # item['win_count'] = info.select('td div[class="Text Left"]').get_text()
            # item['lose_count'] = info.xpath('./td//span/text()').extract_first()
            info = info.select('td')[6].get_text()
            item['win_rate']= info.replace('\n',"")[-3:]
            yield item
