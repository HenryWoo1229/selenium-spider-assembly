#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
 @author   henryWoo
 @date     2020-03-28 16:43
 
 @file     expert.py
 @proj     spider-selenium-assemble
"""

from base_model.base_info import Info


class Expert(Info):
    def __init__(self):
        super().__init__()
        self.writer_name = ''
        self.read_c = ''
        self._time = ''

    @property
    def writer(self):
        return self.writer_name

    @writer.setter
    def writer(self, s):
        self.writer_name = s

    @property
    def read_count(self):
        return self.read_c

    @read_count.setter
    def read_count(self, s):
        self.read_c = s

    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, s):
        self._time = s


if __name__ == '__main__':
    pass
