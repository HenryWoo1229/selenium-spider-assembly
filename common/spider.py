#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
 @author   henryWoo
 @date     2020-03-28 21:04
 
 @file     spider.py
 @proj     spider-selenium-assemble
"""

import os
import sys
import time
from selenium import webdriver


class Spider(object):
    def __init__(self, driver: webdriver.Chrome):
        self._driver = driver
        self.page_count = 1
        self.max_page = 1
        self.next_page_ele = None

    def driver(self):
        return self._driver

    def find_ele_by_css(self, css):
        try:
            return self._driver.find_element_by_css_selector(css)
        except:
            return None

    def find_eles_by_css(self, css):
        try:
            elements = self._driver.find_elements_by_css_selector(css)
        except:
            return None
        return elements if len(elements) > 0 else None

    def max_page_count(self, count):
        self.max_page = count

    def next_page_element_css(self, css):
        self.next_page_ele = self.find_ele_by_css(css)
        if self.next_page_ele is None:
            print('next page element is None')

    def next_page(self):
        if self.page_count < self.max_page:
            if self.next_page_ele is not None:
                self.next_page_ele.click()
                self.page_count += 1
                return True
            else:
                print('must set next page element by SpiderUtil.next_page_element')
                return False
        else:
            return False


if __name__ == '__main__':
    pass
