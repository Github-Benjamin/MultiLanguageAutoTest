#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Benjamin
# @Time   : 2020/4/30 11:14

import xlwt

# table 参数为读取excle后的表格
# 写入文件改变样式操作
def write(x,y,str,styleNum,table):
    # 第二步  设置样式
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = styleNum
    # 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta, 7 = Cyan, 16 = Maroon,
    style = xlwt.XFStyle()
    style.pattern = pattern
    table.write(x, y, str, style)
    return style
