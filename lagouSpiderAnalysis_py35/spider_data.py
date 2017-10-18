#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/10/12 19:51
# @Author  : RookieDay
# @Site    : 
# @File    : spider_data.py
# @Software: PyCharm Community Edition

from lagouSpiderAnalysis_py35 import *
import urllib,json,time,logging
import urllib.parse,urllib.request

logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='spiderLog.txt',
                filemode='w')

# 获取总页数
def get_page_num(res_data):
    data = json.loads(res_data)
    page_num = 0
    if 'content' in data:
        content = data['content']
        if 'positionResult' in content:
            positionResult = content['positionResult']
            totalCount, resultSize = positionResult['totalCount'], positionResult['resultSize']
            if resultSize > 0:
                page_num = int(totalCount / resultSize) + 1
    return page_num

if __name__ == '__main__':
    # 获取常量
    position = data_config.SPIDER_CONFIG['position']
    city = data_config.SPIDER_CONFIG['city']
    district = data_config.SPIDER_CONFIG['district']
    output_file = data_config.SPIDER_CONFIG['output_file']
    row_title = data_config.SPIDER_CONFIG['rowTitle']

    # 实例
    spider = spider_class.SpiderLaGou(position, city, district)
    spider.write_line(output_file, row_title,'w')

    # 参数
    position_format = urllib.parse.quote(spider.position)
    city_format = urllib.parse.quote(spider.city)
    district_format = urllib.parse.quote(spider.district)

    formdata_pram = {
        'first': 'true',
        'pn': 1,
        'kd': spider.position
    }

    # url
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Accept-Language': 'zh-CN,zh;q=0.8',
        'Host': 'www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_' + position_format + '?px=' + spider.px + '&city=' + city_format + '&district=' + district_format,
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/61.0.3163.100 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }
    url = ('https://www.lagou.com/jobs/positionAjax.json?px=' + spider.px + '&city=' + city_format +
           '&district=' + district_format + '&needAddtionalResult=false&isSchoolJob=0')

    print(url)
    # 获取response data 和 页数
    res_data = spider.spider_data(url, headers, formdata_pram).decode('utf-8')
    result_num = parse_res_tools.parse_resdata(res_data,spider,output_file)
    time.sleep(1)
    page_count = get_page_num(res_data)

    for i in range(2,page_count):
        query_param = {
            'first': 'true',
            'pn': i,
            'kd': spider.position
        }
        res_data = spider.spider_data(url, headers, query_param).decode('utf-8')
        # print(res_data)
        result_num += parse_res_tools.parse_resdata(res_data,spider,output_file)
        # print(result_num)
        logging.debug('解析第' + str(i) + '页数据')
        logging.debug('已获取' + str(result_num) + '条的数据')
        time.sleep(2)
