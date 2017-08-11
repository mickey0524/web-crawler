# -*- coding: utf-8 -*-
# 爬取豆瓣电影
__author__ = 'mickey';

import scrapy;
from douban_movie.items import DoubanMovieItem;
import urllib;
import json;

class doubanSpider(scrapy.Spider):

  name = 'douban_movie_spider';
  allowed_domains = ['douban.com']
  start_list = [];
  for i in range(1, 2):
    url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=' + str(i * 20);
    start_list.append(url);
  start_urls = start_list;

  # 这个函数可以注释掉，scrapy默认爬取start_urls内的url，然后对response调用parse方法解析，这个函数的意义在于对request可以做一些修改
  def start_requests(self):
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36';
    headers = { 'User-Agent': user_agent, 'Referer': 'https://movie.douban.com/' };
    for url in self.start_urls:
      yield scrapy.Request(url = url, headers = headers, method = 'GET', callback = self.parse);

  # 解析python爬取出来的资源
  def parse(self, response):
    json_string = response.body.decode('utf-8');
    content = json.loads(json_string);
    for movie in content['subjects']:
      item = DoubanMovieItem();
      item['movie_info'] = movie['url'];
      item['movie_pic'] = movie['cover'];
      item['movie_title'] = movie['title'];
      item['movie_score'] = movie['rate'];
      filename = item['movie_title'].encode('utf-8') + '_' + item['movie_score'].encode('utf-8') + '分.jpg';
      pic = urllib.urlopen(item['movie_pic']);
      data = pic.read();
      try:
        f = open(filename, 'wb');
        f.write(data);
      except IOError, e:
        if hasattr(e, 'reason'):
          print '存图片出现问题', e.reason
      finally:
        f.close();
      yield item;
