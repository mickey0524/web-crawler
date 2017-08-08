# -*- coding: utf-8 -*-
# 爬取虎扑帖子
__author__ = 'mickey';

from bs4 import BeautifulSoup;
import re;
import requests;

class HUBBS:

  def __init__(self, url):
    self.url = url;
    self.bs = '';

  def get_page(self):
    url = self.url;
    r = requests.get(url);
    r.encoding = 'utf-8';      # requests默认采用ISO-8859-1的编码方式，虎扑的网站使用的是utf-8，设置一下就好了
    self.bs = BeautifulSoup(r.text, 'lxml');

  def get_title(self):
    print self.bs.title.string + '\n';

  def get_attention(self):
    print self.bs.find(class_='browse').string + '\n';  # class是python的关键词，所以写成class_，id的话，直接写id=‘xx’就行

  def get_all_comment(self):
    comment_list = self.bs.select(".floor");
    for comment in comment_list:
      user_name = comment.select('.u')[0].string;
      comment_time = comment.select('.left > .stime')[0].string;
      like_num = comment.select('.ilike_icon_list .stime');
      if like_num:
        like_num = like_num[0].string;
      else:
        like_num = '我是楼主';
      content_list = comment.select('.case')[0].stripped_strings;
      content = '';
      for item in content_list:
        content += item

      print user_name, comment_time, like_num, content, '\n'


spider = HUBBS('https://bbs.hupu.com/19949432.html');
spider.get_page();
spider.get_title();
spider.get_attention();
spider.get_all_comment();