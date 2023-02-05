from pathlib import Path

import scrapy
from datetime import date

class ApmexSpider(scrapy.Spider):
    name = "apmex"

    def start_requests(self):
        urls = [
            'https://www.apmex.com/product/11950/1-oz-gold-bar-credit-suisse-in-assay',
            'https://www.apmex.com/product/60162/1-oz-gold-bar-apmex-tep',
            'https://www.apmex.com/product/81534/1-oz-gold-bar-valcambi-in-assay'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {
            'date': date.today(),
            'product': response.xpath('/html/body/main/div/div[1]/section/div[1]/div[1]/h1/text()').get().strip(),
            'price': response.xpath('/html/body/main/div/div[1]/section/div[2]/div[2]/p[1]/text()').get()
        }
        