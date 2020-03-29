#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
 @auchor   henryWoo
 @date     2020-03-28 20:55
 
 @file     spider_util.py
 @proj     spider-selenium-assemble
"""

import os
import sys
import time


class SpiderUtil(object):
    def __init__(self, driver):
        self.page_count = 1
        self.driver = driver
        self.max_page = 1
        self.next_page_ele = None

    def max_page_count(self, count):
        self.max_page = count

    def next_page_element(self, ele):
        self.next_page_ele = ele

    def next_page(self):
        if self.page_count < self.max_page:
            if not self.next_page_ele:
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
