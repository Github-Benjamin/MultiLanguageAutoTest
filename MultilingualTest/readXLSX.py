#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Benjamin
# @Time   : 2020/4/27 20:14

import xlrd
import oneTest
import writeUtils
from xlutils.copy import copy


# 逻辑梳理

# 获取xlsx的值
# 获取所有key，key值
# 获取key那一列多语言值列表

# 获取 Android res 多语言string.xml文件
# 根据 name 获取多语言的xml中的value值，返回列表

# 判断
# 根据xlsx中的key值，获取string.xml文件  列表对比不同
# 打印行号，keyname，成功就不显示信息，对比不通过就打印详细信息



class diffXLSXandXML():

    writeUtils.initXLEX()

    # 定义多语言测试写入的多语言验证xlsx
    diffXLSX = "testXLSX.xlsx"
    book = xlrd.open_workbook(diffXLSX)
    sheet = book.sheets()[0]
    wbXLSX = copy(book)
    wsXLSX = wbXLSX.get_sheet(0)

    diffXML = "testXML.xlsx"
    bookXML = xlrd.open_workbook(diffXML)
    sheetXML = bookXML.sheets()[0]
    wbXML = copy(bookXML)
    wsXML = wbXML.get_sheet(0)


    def __init__(self,path,CountryList,CountryConfig,begFilePath,sheetName):
        self.path = path
        self.CountryList = CountryList
        self.CountryConfig = CountryConfig
        self.begFilePath = begFilePath
        self.sheetName = sheetName


    def getXLSXdict(self):
        file_path = r'%s'%self.begFilePath
        data = xlrd.open_workbook(file_path)

        # 获取表格名称
        table = data.sheet_by_name(self.sheetName)
        keyList = table.col_values(0)  # 获取从第一列开始所有行的值

        keyIndex = []  # 获取key的行号
        keyValue = []  # 获取key的值
        xlsxDict = {}  # 获取key对应的valueList
        beg = 0
        for i in keyList:
            if beg > 0:
                if len(i) > 0:
                    keyIndex.append(beg)
                    keyValue.append(i)
                    xlsxDict[i] = table.row_values(beg,1)  # 获取xx行第2列后面的所有值
            beg += 1
        return keyIndex, keyValue, xlsxDict


    def diffDict(self,xlsx, xml, keyName, keyLine, x):
        print("key:    %s  line:    %s" % (keyName, keyLine + 1))
        if xlsx != xml:
            print("error")
            print("xlsx:    ", xlsx)
            print("xml: ", xml)
        else:
            print("sucess")

        # 数据对比后写入指定文件操作
        y = 1
        for xlsxValue, xmlValue in zip(xlsx, xml):
            # 移除xlsx读取时的首个空格
            xlsxIter = xlsxValue.replace(" ", "")
            try:
                xmlIter = xmlValue.replace(" ", "")
            except Exception as e:
                xmlIter = ""

            if xlsxIter != xmlIter:
                if xlsxIter.capitalize() == xmlIter.capitalize():
                    writeUtils.write(x, y, xlsxValue, 5, self.wsXLSX)

                    writeUtils.write(x, y, xmlValue, 5, self.wsXML)

                else:
                    writeUtils.write(x, y, xlsxValue, 2, self.wsXLSX)

                    writeUtils.write(x, y, xmlValue, 2, self.wsXML)

            elif xlsxIter == xmlIter:
                writeUtils.write(x, y, xlsxValue, 3, self.wsXLSX)

                writeUtils.write(x, y, xmlValue, 3, self.wsXML)

            y += 1


    def getXMLValueList(self,keyname):
        # 获取xml中所有key的值，并进行单个的key-List对比
        doAllXML = oneTest.doAllXML(self.path,self.CountryList,self.CountryConfig,keyname)
        xmlValueList = doAllXML.getAllXMLValue()
        return xmlValueList


    def domain(self):

        # 获取xlsx中的 key和多语言字段
        keyIndex, keyValue, xlsxDict = self.getXLSXdict()

        x = 0
        for keyname in keyValue:
            xlsxLine = keyIndex[keyValue.index(keyname)]
            xlsxKeyValueList = xlsxDict.get(keyname)

            # 获取xml中所有key的值，并进行单个的key-List对比
            xmlValueList = self.getXMLValueList(keyname)

            # 表每行写入Key
            writeUtils.write(x, 0, keyname, 1, self.wsXLSX)
            writeUtils.write(x, 0, keyname, 1, self.wsXML)

            self.diffDict(xlsxKeyValueList, xmlValueList, keyname, xlsxLine, x)
            x += 1
            print()
        self.wbXLSX.save(self.diffXLSX)
        self.wbXML.save(self.diffXML)


if __name__ == "__main__":
    diffXLSXandXML = diffXLSXandXML("多语言.xlsx","应用锁")
    diffXLSXandXML.domain()



