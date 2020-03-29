#!/usr/bin/env python
# -*- coding: utf-8 -*- 

"""
 @author   henryWoo
 @date     2020-03-28 20:14
 
 @file     expert_csv.py
 @proj     spider-selenium-assemble
"""

from common.csv import CSV


class ExpertCSV(CSV):
    def __init__(self):
        super().__init__()
        header = f'文章标题{self.COMMA}阅读数{self.COMMA}时间{self.COMMA}作者\n'
        self.file_writer.write(header)

    def write(self, info):
        string = f'{self.clear_comma(info.title)}{self.COMMA}' \
            f'{self.clear_comma(info.read_count)}{self.COMMA}' \
            f'{self.clear_comma(info.time)}{self.COMMA}' \
            f'{self.clear_comma(info.writer)}{self.COMMA}\n'
        self.file_writer.write(string)


if __name__ == '__main__':
    pass
