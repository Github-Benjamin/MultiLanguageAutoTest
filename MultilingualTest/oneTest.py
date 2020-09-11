#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Benjamin
# @Time   : 2020/4/26 18:01

from xml.dom.minidom import parse
import xml.dom.minidom


# 多语言的xlsx中的国家排序
# CountryList = ["zh","en","ru","ar","zhHk","hi","th","in","fr","vi","pt","es"]

# CountryList = ["zh","en","ru","ar","zh","hi","th","in","fr","vi","pt","es"]
# CountryList = ["zh","en","ar","hi","ru","vi","pt","th","in","zhHk","zhTW","fr","es","ja","ko","de"]
CountryList = ["zh",	"en",	"ar",	"hi",	"ru",	"vi",	"pt",	"th",	"in",	"zhTW", "zhTW",	"fr",	"es"]
CountryConfig = {
            "zh": "values-zh",
            "zhHk": "values-zh-rHK",
            "zhTW": "values-zh-rTW",
            "en": "values",
            "vi": "values-vi",
            "ru": "values-ru",
            "pt": "values-pt",
            "in": "values-in",
            "es": "values-es",
            "fr": "values-fr",
            "hi": "values-hi",
            "th": "values-th",
            "it": "values-it",
            "tr": "values-tr",
            "fi": "values-fi",
            "ar": "values-ar",
            "ja":"values-ja",
            "ko":"values-ko",
            "de":"values-de"
        }

class doAllXML():
    def __init__(self,path,CountryList,CountryConfig,keyName):
        self.path = path
        self.CountryList = CountryList
        self.CountryConfig = CountryConfig
        self.keyName = keyName
        # 不同国家对应的目录文件
        # self.CountryConfig = {
        #     "zh": "values-zh",
        #     "zhHk": "values-zh-rHK",
        #     "zhTW": "values-zh-rTW",
        #     "en": "values",
        #     "vi": "values-vi",
        #     "ru": "values-ru",
        #     "pt": "values-pt",
        #     "in": "values-in",
        #     "es": "values-es",
        #     "fr": "values-fr",
        #     "hi": "values-hi",
        #     "th": "values-th",
        #     "it": "values-it",
        #     "tr": "values-tr",
        #     "fi": "values-fi",
        #     "ar": "values-ar",
        #     "ja":"values-ja",
        #     "ko":"values-ko",
        #     "de":"values-de"
        #
        # }

    def getXML(self,Country):
        # 使用minidom解析器打开 XML 文档
        file = self.path + "/res/%s/strings.xml" % self.CountryConfig.get(Country)
        DOMTree = xml.dom.minidom.parse(file)
        collection = DOMTree.documentElement

        # 在集合中key
        content = collection.getElementsByTagName("string")
        return content


    def getXMLName(self,content):
        for item in content:
            if self.keyName == item.getAttribute("name"):
                try:
                    return item.childNodes[0].data
                except Exception as e:
                    return None


    def getXMLValue(self,content):
        keyList = []
        for item in content:
            if self.keyName in item.childNodes[0].data or self.keyName == item.childNodes[0].data:
                # print(self.keyName, item.getAttribute("name"))
                keyList.append(item.getAttribute("name"))
        return keyList



    def getSearchKey(self):
        keyList = []
        for country in self.CountryList:
            content = self.getXML(country)
            CountryKeyList = self.getXMLValue(content)
            if len(CountryKeyList) > 0:
                for key in CountryKeyList:
                    if key not in keyList:
                        keyList.append(key)
        return keyList

    def getSearchValue(self):
        searchStr = ""
        for key in self.getSearchKey():
            self.keyName = key
            searchStr += self.getAllXMLValue(1) + "\n"
            print("\n")
        return searchStr


    def getAllXMLValue(self,testPrint=None):
        valueList = []

        if testPrint:
            xmlStr = ""
            xmlStr += "\n" + "key:    " + str(self.keyName)
            print(xmlStr)

        for country in self.CountryList:
            content = self.getXML(country)
            value = self.getXMLName(content)
            if testPrint:
                xmlStr += "\n" + country + ":    " + str(value)
                print(country, ":    ", value)
            valueList.append(value)

        if testPrint:
            return xmlStr

        return valueList


if __name__ == "__main__":

    #   获取单个key的 所有国家值
    name = "取消"

    readAllXML = doAllXML("CleanLite_2.0.0(v3)_release-signed",CountryList,CountryConfig,name)

    # 精装匹配key
    # keyList = readAllXML.getAllXMLValue(1)

    # 模块匹配，文字搜索全部多语言
    keyList = readAllXML.getSearchValue()

