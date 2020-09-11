#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Benjamin
# @Time   : 2020/8/7 19:19


import xlrd


class readXlsx():


    def __init__(self,filePath,sheetName,x = 0, y = 1):
        self.filePath = filePath
        self.sheetName = sheetName
        self.x = x
        self.y = y


    # 获取xlsx数据
    def getXlsxData(self):
        # 加载文件
        readfilePath = r"%s" % self.filePath
        xlsxData = xlrd.open_workbook(readfilePath)
        return xlsxData


    # 获取指定表格的数据
    def getSheetNameData(self,data):
        # 获取表格名称
        tableData = data.sheet_by_name(self.sheetName)
        return tableData



    # 读取行，读取列
    def getXlsxRanks(self,table):

        # x为列，y为行

        keyList = table.col_values(self.x)  # 获取从第一列开始所有行的值

        keyIndex = []  # 获取key的行号
        keyValue = []  # 获取key的值
        xlsxDict = {}  # 获取key对应的valueList
        beg = 0
        for i in keyList:
            if beg > 0:
                if len(i) > 0:
                    keyIndex.append(beg)
                    keyValue.append(i)
                    xlsxDict[i] = table.row_values(beg,self.y)  # 获取xx行第2列后面的所有值，从0开始计数
            beg += 1

        return keyIndex, keyValue, xlsxDict


    # 函数汇总
    def domain(self):
        try:
            getXlsxData = self.getXlsxData()
            getSheetNameData = self.getSheetNameData(getXlsxData)
            getXlsxRanks = self.getXlsxRanks(getSheetNameData)
            return getXlsxRanks
        except Exception as e:
            print("readXlsx Error:\n", e)


if __name__ == "__main__":
    diffXLSXandXML = readXlsx("../stringtest.xlsx","Sheet1")
    data = diffXLSXandXML.domain()
    print(data)


