# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import os
import uuid
path=r'半身美女'
class BaiduspiderPipeline(object):
    def process_item(self, item, spider):
        str_table = {
            '_z2C$q': ':',
            '_z&e3B': '.',
            'AzdH3F': '/'
        }
        char_table = {
            'w': 'a',
            'k': 'b',
            'v': 'c',
            '1': 'd',
            'j': 'e',
            'u': 'f',
            '2': 'g',
            'i': 'h',
            't': 'i',
            '3': 'j',
            'h': 'k',
            's': 'l',
            '4': 'm',
            'g': 'n',
            '5': 'o',
            'r': 'p',
            'q': 'q',
            '6': 'r',
            'f': 's',
            'p': 't',
            '7': 'u',
            'e': 'v',
            'o': 'w',
            '8': '1',
            'd': '2',
            'n': '3',
            '9': '4',
            'c': '5',
            'm': '6',
            '0': '7',
            'b': '8',
            'l': '9',
            'a': '0'
        }
        char_table = {ord(key): ord(value) for key, value in char_table.items()}
        for key, value in str_table.items():
            item['img_url'] = item['img_url'].replace(key, value)
        item['img_url'] = item['img_url'].translate(char_table)
        try:
            if item['img_url'].startswith('http'):
                response=requests.get(item['img_url'],timeout=3)
                if response.status_code==200:
                    with open(os.path.join(path, str(uuid.uuid1()).replace('-', '_') + '.jpg'), 'wb') as f:
                        f.write(response.content)
                return None
            return None
        except ConnectionError:
            return None

