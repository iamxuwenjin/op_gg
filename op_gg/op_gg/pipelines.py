# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
from op_gg.items import HeroItem,BanItem,PickItem,PlayerItem
from scrapy.exporters import CsvItemExporter


class ConPipeline(object):
    def process_item(self, item, spider):
        item['source'] = spider.name
        item['utc_time'] = str(datetime.utcnow())
        return item

class HeroInfoPipeline(object):
    def open_spider(self, spider):
        self.filename = open("hero_info.csv", "wb")
        # 创建一个csv文件读写对象，参数是需要保存数据的csv文件对象
        self.csv_exporter = CsvItemExporter(self.filename)
        # 表示开始进行数据写入
        self.csv_exporter.start_exporting()

    def process_item(self, item, spider):
        if isinstance(item,HeroItem):
            self.csv_exporter.export_item(item)
        return item

    def close_spider(self, spider):
        # 表示结束数据写入
        self.csv_exporter.finish_exporting()
        self.filename.close()

class PickPipeline(object):
    def open_spider(self, spider):
        self.filename = open("pick_info.csv", "wb")
        # 创建一个csv文件读写对象，参数是需要保存数据的csv文件对象
        self.csv_exporter = CsvItemExporter(self.filename)
        # 表示开始进行数据写入
        self.csv_exporter.start_exporting()

    def process_item(self, item, spider):
        if isinstance(item,PickItem):
            self.csv_exporter.export_item(item)
        return item

    def close_spider(self, spider):
        # 表示结束数据写入
        self.csv_exporter.finish_exporting()
        self.filename.close()

class BanPipeline(object):
    def open_spider(self, spider):
        self.filename = open("ban_info.csv", "wb")
        # 创建一个csv文件读写对象，参数是需要保存数据的csv文件对象
        self.csv_exporter = CsvItemExporter(self.filename)
        # 表示开始进行数据写入
        self.csv_exporter.start_exporting()

    def process_item(self, item, spider):
        if isinstance(item,BanItem):
            print '---------------------'
            self.csv_exporter.export_item(item)
        return item

    def close_spider(self, spider):
        # 表示结束数据写入
        self.csv_exporter.finish_exporting()
        self.filename.close()

class PlayerPipeline(object):
    def open_spider(self, spider):
        self.filename = open("player_info.csv", "wb")
        # 创建一个csv文件读写对象，参数是需要保存数据的csv文件对象
        self.csv_exporter = CsvItemExporter(self.filename)
        # 表示开始进行数据写入
        self.csv_exporter.start_exporting()

    def process_item(self, item, spider):
        if isinstance(item,PlayerItem):
            self.csv_exporter.export_item(item)
        return item

    def close_spider(self, spider):
        # 表示结束数据写入
        self.csv_exporter.finish_exporting()
        self.filename.close()