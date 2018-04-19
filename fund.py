#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: mickey0524
# 爬取私募基金
# 2018-04-18

import time
import re
import requests
import os
import sys
from selenium import webdriver

FUND_URL = 'http://gs.amac.org.cn/amac-infodisc/res/pof/securities/index.html'
FETCH_DATA_PREFIX = 'http://gs.amac.org.cn/amac-infodisc/api/pof/securities/'
headers = {
    'Referer': 'http://gs.amac.org.cn/amac-infodisc/res/pof/securities/detail.html?id=1804171732101938',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}
key_arr = ['cpmc', 'cpbm', 'gljg', 'slrq', 'dqr',
           'tzlx', 'sffj', 'clgm', 'clscyhs', 'tgjg']
header_arr = [u'产品名称', u'产品编码', u'管理机构',
              u'设立日期', u'到期日', u'投资类型', u'是否分级', u'成立规模（万元）', u'投资者总数', u'托管机构']
SLEEP_INTERVAL = 3
start_time, end_time = None, None


def get_message():
  """
  爬取主函数
  """
  driver = webdriver.PhantomJS()
  # driver = webdriver.Chrome()
  driver.get(FUND_URL)

  from_time_btn = driver.find_element_by_id('foundDateFrom')
  to_time_btn = driver.find_element_by_id('foundDateTo')
  search_btn = driver.find_element_by_xpath(
      "//input[@value='查询']")
  
  from_time_btn.send_keys(start_time)
  to_time_btn.send_keys(end_time)
  search_btn.click()

  time.sleep(SLEEP_INTERVAL)
  
  info_text = driver.find_element_by_id('dvccFundList_info').text
  if info_text == u'没有数据':
    print '没有数据'
    return
  pattern = re.compile(r'\d+')
  max_paginate_num = re.findall(pattern, info_text)[-1]

  while True:
    id_list = []
    for product in driver.find_elements_by_class_name('ajaxify'):
      href = product.get_attribute('href')
      pattern = re.compile(r'[^0-9]')
      id = re.sub(pattern, '', href)
      id_list += id,
    print id_list
    fetch_data(id_list)

    if driver.find_element_by_class_name('current').text == max_paginate_num:
      break
    else:
      driver.find_element_by_class_name('next').click()
      time.sleep(SLEEP_INTERVAL)
  
def fetch_data(id_list):
  """
  获取id_list，用于拉取数据
  type id_list: list id列表
  """
  file_name = 'fund_{start_time}_{end_time}.csv'.format(start_time = start_time, end_time = end_time) 
  with open(file_name, 'a+') as f:
    for id in id_list:
      url = FETCH_DATA_PREFIX + id
      r = requests.get(url, headers=headers)
      data = r.json()
      message = []
      for key in key_arr:
        message += data[key].encode('utf-8'),
      message = ','.join(message)
      message += os.linesep
      f.write(message)


def add_csv_header():
  """
  增加csv文件的行头
  """
  file_name = 'fund_{start_time}_{end_time}.csv'.format(
      start_time=start_time, end_time=end_time)
  with open(file_name, 'a+') as f:
    header = ','.join(header_arr) + os.linesep
    header = header.encode('utf-8')
    f.write(header)


if __name__ == '__main__':
  if len(sys.argv) < 3:
    print '请输入启动时间和终止时间'
    os._exit(1)
  start_time, end_time = sys.argv[1], sys.argv[2]
  pattern = re.compile(r'^\d{4}-\d{2}-\d{2}$')
  if not re.search(pattern, start_time) or not re.search(pattern, end_time):
    print '输入时间或输出时间格式不对, 2018-04-10这样的格式'
    os._exit(1)
  print '开始爬取数据'
  add_csv_header()
  get_message()