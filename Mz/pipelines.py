# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import scrapy
from .settings import IMAGES_STORE as images_store
from scrapy.pipelines.images import ImagesPipeline
import re


def _format(path):
    path = re.sub(r'[？\\*|“<>:/]', '', str(path))
    return path


class MzPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        image_url = item['image_url']
        yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        # print(results)
        image_path = [x['path'] for ok, x in results if ok]
        image_name = item['image_url'].split('/')[-1]

        new_path = images_store + _format(item["cate_name"])

        if os.path.exists(new_path):
            os.rename(images_store +
                      image_path[0], new_path + '/' + image_name)
        else:
            os.makedirs(new_path)
            os.rename(images_store +
                      image_path[0], new_path + '/' + image_name)
