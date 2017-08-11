# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanMoviePipeline(object):

  def __init__(self):
    self.file = open('movie.txt', 'w+');

  def process_item(self, item, spider):
    movie_mes = 'title：' + item['movie_title'].encode('utf-8') + ' pic：' + item['movie_pic'].encode('utf-8') + ' info：' + item['movie_info'].encode('utf-8') + ' score：' + item['movie_score'].encode('utf-8') + '\n';
    try:
      self.file.write(movie_mes);
    except IOError as e:
      if hasattr(e, 'reason'):
        print '文件存储错误: ', e;
    return item;

  def close_spider(self, spider):
    self.file.close();
