# -*- coding: utf-8 -*-
import scrapy
import json
import time
from urllib.parse import urlencode
from baiduspider.items import BaiduspiderItem
class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['img.baidu.com']
    start_urls = ['http://img.baidu.com/']
    def start_requests(self):
        base_url='http://image.baidu.com/search/acjson?'
        for page in range(30,1200,30):
            timestamp = int(round(time.time() * 1000))
            data={
            'tn': 'resultjson_com',
            'ipn': 'rj',
            'ct': '201326592',
            'is':None,
            'fp': 'result',
            'queryWord': '证件照',
            'cl': '2',
            'lm': '-1',
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid':None,
            'st': '-1',
            'z':None,
            'ic': '0',
            'hd': '0',
            'latest': '0',
            'copyright':'0',
            'word': '证件照',
            's':None,
            'se':None,
            'tab':None,
            'width':None,
            'height':None,
            'face': '0',
            'istype': '2',
            'qc':None,
            'nc': '1',
            'fr':None,
            'expermode':None,
            'force':None,
            'pn': page,
            'rn': '30',
            'gsm': '1e',
            '%s'%(timestamp):None
        }
            url=base_url+urlencode(data)
            yield scrapy.Request(url=url, callback=self.parse_html)

    def parse_html(self, response):
        item=BaiduspiderItem()
        html=json.loads(response.text)
        if html:
            results=html['data']
            for result in results:
                try:
                    item['img_url']=result['objURL']
                    yield item
                except:
                    pass









