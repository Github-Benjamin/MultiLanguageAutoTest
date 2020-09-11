#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Benjamin
# @Time   : 2020/8/7 17:46

from  utils import readXlsxUtils
from  utils import writeUtils
from  utils import oneTest
import xlrd
from xlutils.copy import copy


class diff():

    # 定义多语言测试写入的多语言验证xlsx
    diffXLSX = "testXLSX.xlsx"
    book = xlrd.open_workbook(diffXLSX)
    sheet = book.sheets()[0]
    wb = copy(book)
    ws = wb.get_sheet(0)

    diffXML = "testXML.xlsx"
    bookXML = xlrd.open_workbook(diffXML)
    sheetXML = bookXML.sheets()[0]
    wbXML = copy(bookXML)
    wsXML = wbXML.get_sheet(0)


    def __init__(self,fllePath,SheetName,CountryList ,xLine = 0,yLine = 1):
        self.fllePath = fllePath
        self.SheetName = SheetName

        self.CountryList = CountryList

        self.xLine = xLine
        self.yLine = yLine



        self.keyName = None
        self.keyLine = None
        self.x = None
        self.xlsx = None
        self.xml = None


    def getPrint(self):
        print("key:    %s  line:    %s" % (self.keyName, self.keyLine + 1))
        if self.xlsx != self.xml:
            print("diff error:")
            print("xlsx:    ", self.xlsx)
            print("xml: ", self.xml)
        else:
            print("diff sucess.")


    # 数据对比并写入
    def getXlsxXmlDiff(self,x):
        # x列，y行
        y = 1 # 行
        for xlsxValue, xmlValue in zip(self.xlsx, self.xml):
            self.getDiffWrite(xlsxValue, xmlValue, x,y)
            y += 1    # 每次下一行写入数据


    # 字符串替换
    def getReplaceValue(self,data):
        # 移除xlsx读取时的首个空格,所有空格
        # 移除xml字符串中的空格
        try:
            return data.replace(" ", "")
        except Exception as e:
            print("getReplaceValue Error: ",e)
            print("data is: ",data)


    # 判断 xlsxIter与xmlIter 元素是否一致的写入规则
    def getDiffWrite(self,xlsxValue,xmlValue,x,y):

        xlsxIter = self.getReplaceValue(xlsxValue)
        xmlIter = self.getReplaceValue(xmlValue)

        if xlsxIter != xmlIter:

            # capitalize() 首字母大写
            if xlsxIter.capitalize() == xmlIter.capitalize():
                writeUtils.write(x, y, xlsxValue, 5, self.ws)    # 根据列行，写入单坐标的数据xlsx原始数据
                writeUtils.write(x, y, xmlValue, 5, self.wsXML)    # 根据列行，写入单坐标的数据xml实际数据
            else:
                writeUtils.write(x, y, xlsxValue, 2, self.ws)
                writeUtils.write(x, y, xmlValue, 2, self.wsXML)

        elif xlsxIter == xmlIter:
            writeUtils.write(x, y, xlsxValue, 3, self.ws)
            writeUtils.write(x, y, xmlValue, 3, self.wsXML)


    # 获取xmlValueList
    def getXmlValueList(self,keyName):
        # 获取xml中所有key的值，并进行单个的key-List对比
        doAllXML = oneTest.doAllXML(self.CountryList, keyName)
        xmlValueList = doAllXML.getAllXMLValue()
        return xmlValueList


    # 获取xlsxValue数据
    def getXlsxValue(self):
        diffXLSXandXML = readXlsxUtils.readXlsx(self.fllePath, self.SheetName,self.xLine,self.yLine)
        keyIndex, keyValue, xlsxDict = diffXLSXandXML.domain()
        return keyIndex, keyValue, xlsxDict


    # 设置初始化的值
    def setXlsxXmlValue(self,xlsxDict,keyIndex,keyValue,keyName):
        self.keyName = keyName
        self.keyLine = keyIndex[keyValue.index(keyName)]
        self.xlsx = xlsxDict.get(keyName)

        # 获取xml中所有key的值，并进行单个的key-List对比
        self.xml = self.getXmlValueList(keyName)



    def doMain(self):

        keyIndex, keyValue, xlsxDict = self.getXlsxValue()

        if len(keyIndex) == 0:
            print("getXlsxValue Error")

        x = 0 # 从第0行开始
        for keyName in keyValue:

            # 表每行写入Key
            writeUtils.write(x, 0, keyName, 1, self.ws)
            writeUtils.write(x, 0, keyName, 1, self.wsXML)

            self.setXlsxXmlValue(xlsxDict,keyIndex,keyValue,keyName)
            self.getPrint()
            self.getXlsxXmlDiff(x)

            x += 1
            print()

        self.wb.save(self.diffXLSX)
        self.wbXML.save(self.diffXML)


if __name__ == "__main__":
    xxx = diff("../test.xlsx","Sheet1",1,2)
    xxx.doMain()
