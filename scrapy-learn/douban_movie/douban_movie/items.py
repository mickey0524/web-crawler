# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanMovieItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movie_title = scrapy.Field();
    movie_score = scrapy.Field();
    movie_pic = scrapy.Field();
    movie_info = scrapy.Field();
