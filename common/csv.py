#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
 @auchor   henryWoo
 @date     2020-03-28 20:09
 
 @file     csv.py
 @proj     spider-selenium-assemble
"""

import os
import time


class CSV(object):
    def __init__(self, filename=None, comma=','):
        if not filename:
            filename = '{}/{}.csv'.format(os.getcwd(), time.time())
        self.file_writer = open(file=filename, mode='a', encoding='utf-8', errors='ignore')
        self.COMMA = comma

    def write(self, info):
        pass

    def close_writer(self):
        self.file_writer.close()

    def clear_comma(self, string):
        return string.replace(self.COMMA, ' ') if self.COMMA in string else string


if __name__ == '__main__':
    pass
