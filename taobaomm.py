# -*- coding: utf-8 -*-
# 爬取淘宝MM
__author__ = 'mickey';

import urllib;
import urllib2;
import re;
import os;

class TBMM:

  def __init__(self, base_url, page_num):
    self.base_url = base_url;
    self.page_num = page_num;

  def get_page(self):
    url = self.base_url + '?page=' + str(self.page_num);
    try:
      request = urllib2.Request(url);
      response = urllib2.urlopen(request);
      content = response.read().decode('gbk');
      return content;
    except urllib2.URLError, e:
      if hasattr(e, 'reason'):
        print '爬取淘宝MM出现错误，错误原因是', e.reason;
      return None;

  def get_mm_mes(self, content):
    pattern = re.compile(r'<div class="list-item.*?<a.*?lady-avatar.*?<img src="(.*?)".*?<a class="lady-name.*?href="(.*?)".*?>(.*?)</a>.*?<strong>(.*?)</strong>.*?<span>(.*?)</span>', re.S);
    contents = re.findall(pattern, content);
    for item in contents:
      self.make_dir(item[2]);
      self.save_img(item[0], item[2]);
      self.save_txt(item);

  def make_dir(self, name):
    if os.path.exists(name):
      return ;
    os.makedirs(name);

  def save_img(self, img_url, file_name):
    img_url = 'http:' + img_url;
    u = urllib.urlopen(img_url);
    data = u.read();
    back_suffix = img_url[img_url.rindex('.'):];
    file_name = file_name + '/' + file_name;
    file_name += back_suffix;
    try:
      f = open(file_name, 'wb')
      f.write(data)
    except IOError, e:
      if hasattr(e, 'reason'):
        print '存图片出现问题', e.reason
    finally:
      f.close()

  def save_txt(self, content):
    name = content[2];
    file_name = name + '/' + name + '.txt';
    save_content = 'mm的名字是' + content[2].encode('utf-8') + '，今年' + content[3].encode('utf-8') + '岁，现居住在' + content[4].encode('utf-8') + '头像为' + content[0].encode('utf-8') + '，个人页面为' + content[1].encode('utf-8');
    try:
      f = open(file_name, 'w+');
      f.write(save_content);
    except IOError, e:
      if hasattr(e, 'reason'):
        print '文本存储出现问题', e.reason
    finally:
      f.close()

  def start(self):
    content = self.get_page();
    self.get_mm_mes(content);

spider = TBMM('https://mm.taobao.com/json/request_top_list.htm', 1);
spider.start();


