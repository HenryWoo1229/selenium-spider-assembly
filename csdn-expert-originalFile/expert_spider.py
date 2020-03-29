#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
 @author   henryWoo
 @date     2020-03-28 20:35
 
 @file     expert_spider.py
 @proj     spider-selenium-assemble
"""

from selenium import webdriver

from comman.expert_csv import ExpertCSV
from common.spider import Spider
from model.expert import Expert

url_list = ['https://blog.csdn.net/weixin_43570367?t=1']
csdn_one_page_title_count = 40


def get_writer(url):
    return url.split('/')[-1].split('?')[0]


if __name__ == '__main__':
    spider = Spider(webdriver.Chrome(executable_path='../asset/chromedriver11'))
    driver = spider.driver()

    count = 1
    csv = ExpertCSV()
    try:
        for url in url_list:
            driver.get(url)
            while True:
                for i in range(1, 41):
                    # model 对象
                    expert = Expert()

                    # 获取标题#.article-item-box:nth-child(1) > h4 > a
                    title = spider.find_ele_by_css(f'.article-item-box:nth-child({i}) > h4 > a')
                    if title is not None:
                        print(title.text)
                        expert.title = title.text

                    the_time = spider.find_ele_by_css(f'.article-item-box:nth-child({i}) .date')
                    if the_time is not None:
                        expert.time = the_time.text

                    # 获取阅读数
                    read_count = spider.find_ele_by_css(f'.article-item-box:nth-child({i}) p:nth-child(3) .num')
                    if read_count is not None:
                        expert.read_count = read_count.text

                    # 写入作者链接
                    expert.writer = url
                    csv.write(expert)

                # 下一页按钮控件设置
                spider.next_page_element_css('.js-page-next')

                if count == 1:
                    elements = spider.find_eles_by_css('.ui-pager')
                    if elements is not None:
                        max_page = elements[-3]
                        spider.max_page_count(int(max_page.text))
                    else:
                        print('not found max page')
                    count += 1

                if not spider.next_page():
                    raise Exception()
    except:
        csv.close_writer()
        driver.quit()
