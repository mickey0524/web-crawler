# -*- coding: utf-8 -*-
# 爬取百度贴吧
__author__ = 'mickey';

import urllib2;
import re;

class Tool:
  #去除img标签,7位长空格
  remove_img = re.compile('<img.*?>| {7}|')
  #删除超链接标签
  remove_addr = re.compile('<a.*?>|</a>')
  #把换行的标签换为\n
  replace_line = re.compile('<tr>|<div>|</div>|</p>')
  #将表格制表<td>替换为\t
  replace_td= re.compile('<td>')
  #把段落开头换为\n加空两格
  replace_para = re.compile('<p.*?>')
  #将换行符或双换行符替换为\n
  replace_br = re.compile('<br><br>|<br>')
  #将其余标签剔除
  remove_extra_tag = re.compile('<.*?>')
  def replace(self,x):
    x = re.sub(self.remove_img,"",x)
    x = re.sub(self.remove_addr,"",x)
    x = re.sub(self.replace_line,"\n",x)
    x = re.sub(self.replace_td,"\t",x)
    x = re.sub(self.replace_para,"\n    ",x)
    x = re.sub(self.replace_br,"\n",x)
    x = re.sub(self.remove_extra_tag,"",x)
    #strip()将前后多余内容删除
    return x.strip()

class BDTB:
  # 初始化参数
  def __init__(self, base_url, see_lz, floor_tag):
    self.base_url = base_url;
    self.see_lz = '?see_lz=' + str(see_lz);
    self.tool = Tool();
    self.default_title = u"百度贴吧";
    self.floor_tag = floor_tag;
    self.floor_num = 1;

  def get_page(self, page_num):
    url = self.base_url + self.see_lz + '&pn=' + str(page_num);
    try:
      request = urllib2.Request(url);
      response = urllib2.urlopen(request);
      content = response.read().decode('utf-8');
      return content;
    except urllib2.URLError, e:
      if (hasattr(e, 'reason')):
        print u'连接百度贴吧失败,错误原因', e.reason;
      return None;

  def get_title(self, content):
    pattern = re.compile(r'<h3.*?core_title_txt.*?>(.*?)</h3>', re.S);
    result = re.search(pattern, content);
    if result:
      return result.group(1).strip();
    else:
      return self.default_title;

  def get_page_num(self, content):
    pattern = re.compile(r'<li.*?l_reply_num.*?<span.*?span>.*?<span.*?>(.*?)</span>', re.S);
    result = re.search(pattern, content);
    if result:
      return result.group(1).strip();
    else:
      return None;

  def get_content(self, content):
    pattern = re.compile(r'<div id="post_content_.*?>(.*?)</div>', re.S);
    result = re.findall(pattern, content);
    contents = [];
    if result:
      for item in result:

        # print floor,u"楼------------------------------------------------------------------------------------------------------------------------------------\n"
        content = '\n' + self.tool.replace(item) + '\n';
        contents.append(content.encode('utf-8'));
        # floor += 1;
    return contents;

  def write_txt(self):
    page = self.get_page(1);
    title = self.get_title(page);
    page_num = self.get_page_num(page);
    print '该帖子一共有' + str(page_num) + '页';
    try:
      file = open(title + '.txt', 'w+');
      for i in range(1, int(page_num) + 1):
        page = self.get_page(i);
        contents = self.get_content(page);
        for item in contents:
          if self.floor_tag == '1':
            floor_num = "楼------------------------------------------------------------------------------------------------------------------------------------\n" + str(self.floor_num) + '\n';
            self.floor_num += 1;
            file.write(floor_num);
          file.write(item);
        print str(i) + '页已经写入完毕';
    except IOError, e:
      if hasattr(e, 'reason'):
        print '错误原因', e.reason;
    finally:
      print '该帖子已经全部写入完毕';

  def start(self):
    self.write_txt();


base_url =  'http://tieba.baidu.com/p/3138733512';
see_lz = raw_input('是否只看楼主，1为只看，0不为 ');
floor_tag = raw_input('是否添加分割线，1为分割，0不为 ');
spider = BDTB(base_url, see_lz, floor_tag);
spider.start();

