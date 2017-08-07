# -*- coding: utf-8 -*-
# 爬取糗事百科的热点文章
__author__ = 'mickey';

import urllib;
import urllib2;
import re;

# 糗事百科爬虫类
class QSBK:

  # 初始化部分参数
  def __init__(self):
    self.cur_page = 1;
    self.user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36';
    self.headers = { 'User-Agent': self.user_agent };
    self.cur_items = [];
    self.item_index = 0;
    self.enable = True;

  # 获取一页的数据
  def get_page(self):
    url = 'https://www.qiushibaike.com/hot/page/' + str(self.cur_page);
    request = urllib2.Request(url, headers = self.headers);
    try:
      response = urllib2.urlopen(request);
      content = response.read().decode('utf-8');
      self.cur_page += 1;
      return content;
    except urllib2.URLError, e:
      if hasattr(e, "reason"):
        print u'连接糗事百科失败，失败原因', e.reason;
        return None;

  # 根据得到的一页数据，匹配出每个段子的信息
  def get_page_item(self, content):
    pattern = re.compile(r'<div.*?author.*?>.*?<a.*?<h2>(.*?)</h2>.*?<div.*?content">.*?' +
      '<span>(.*?)</span>.*?<div.*?stats">.*?<i.*?number">(.*?)</i>.*?' +
      '.*?number">(.*?)</i>', re.S);
    items = re.findall(pattern, content);
    self.cur_items = items;
    self.item_index = 0;

  # 输出一个段子
  def get_one_story(self):
    if (self.item_index == len(self.cur_items)):
      self.item_index = 0;
      self.get_page_item(self.get_page());
    item = self.cur_items[self.item_index];
    content = re.sub(r'<br/>', '\n', item[1].strip());
    print u"第%d页\t发布人:%s\t赞:%s\t评论数:%s\n%s" %(self.cur_page, item[0].strip(), item[2], item[3], content)
    self.item_index += 1;

  # 开始爬取
  def start(self):
    print '正在读取糗事百科，按Q退出';
    while (self.enable):
      input = raw_input();
      if (input == 'Q'):
        self.enable = False;
      self.get_one_story();
    print '退出程序';

spider = QSBK();
spider.start();
