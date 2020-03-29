#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
 @author   henryWoo
 @date     2020-03-28 20:00
 
 @file     base_info.py
 @proj     spider-selenium-assemble
"""


class Info(object):
    def __init__(self):
        self.title_name = ''

    @property
    def title(self):
        return self.title_name

    @title.setter
    def title(self, s):
        self.title_name = s


if __name__ == '__main__':
    pass
