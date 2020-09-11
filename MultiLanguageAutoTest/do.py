#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Benjamin
# @Time   : 2020/8/7 21:21

from utils import oneTest
from utils import diffUtils


# 多语言的xlsx中的国家排序
# CountryList = ["zh","en","ru","ar","zhHk","hi","th","in","fr","vi","pt","es"]

CountryList = ["zh","en","ru","ar","zhTW","hi","th","in","fr","vi","pt","es"]
# CountryList = ["zh","en","ar","hi","ru","vi","pt","th","in","zhHk","zhTW","fr","es","ja","ko","de"]


if __name__ == "__main__":

    #   获取单个key的 所有国家值
    name = "boost_permission_btn"
    print("key: %s"%name)
    readAllXML = oneTest.doAllXML(CountryList,name)
    readAllXML.getAllXMLValue(1)


    # 对比数据表格，传输xy坐标，默认 0,1
    # xxx = diffUtils.diff("test.xlsx","Sheet1",CountryList,1,2)
    # xxx.doMain()


