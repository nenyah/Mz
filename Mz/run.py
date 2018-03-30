# -*- coding: utf-8 -*- 
# @Author: Steven 
# @Date: 2018-03-23 10:23:17 
# @Last Modified by: Steven 
# @Last Modified time: 2018-03-23 10:36:47 
# @file: run.py
from scrapy.cmdline import execute
execute("scrapy crawl mzi -o mzi.json".split())
