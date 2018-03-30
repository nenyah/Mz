# -*- coding: utf-8 -*-
import scrapy
from Mz.items import MzItem
from urllib.parse import urljoin

class MziSpider(scrapy.Spider):
    name = "mzi"
    allowed_domains = ["mzitu.com"]
    start_urls = ['http://www.mzitu.com/all/']

    def parse(self, response):
        node_list = response.xpath('//div[@class="all"]//li//a/@href').extract()
        for each in node_list[:2]:
            yield scrapy.Request(each, callback=self.parse_image)


    def parse_image(self, response):
        item = MzItem()
        item['cate_name'] = self._get_cate_name(response)
        item['cate_link'] = self._get_cate_link(response)
        item['page_url'] = response.url
        image_url = response.xpath('//div[@class="main-image"]//a/img/@src').extract()[0]
        item['image_url'] = image_url
        yield item

        next_page = response.xpath('//div[@class="main-image"]//a/@href').extract()[0]
        # print(len(next_page.split('/')))
        if len(next_page.split('/')) >= 5:
            yield scrapy.Request(next_page, callback=self.parse_image)

    def _get_cate_name(self, response):
        '''get cate name, will be the path name in the pipline'''
        return response.xpath('//div[@class="currentpath"]/text()[3]').extract()[0].replace(" » ","")

    def _get_cate_link(self, response):
        if len(response.url.split('/')) == 5:
            link = "http://" + '/'.join(response.url.split('/')[-3:-1])
        elif len(response.url.split('/')) == 4:
            link = response.url
        return link
