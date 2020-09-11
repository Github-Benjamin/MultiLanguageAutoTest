#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Benjamin
# @Time   : 2020/4/26 18:01

from xml.dom.minidom import parse
import xml.dom.minidom


# 多语言的xlsx中的国家排序
# CountryList = ["zh","en","ru","ar","zhHk","hi","th","in","fr","vi","pt","es"]

CountryList = ["zh","en","ru","ar","zhTW","hi","th","in","fr","vi","pt","es"]
# CountryList = ["zh","en","ar","hi","ru","vi","pt","th","in","zhHk","zhTW","fr","es","ja","ko","de"]


class doAllXML():
    def __init__(self,CountryList,keyName):
        self.CountryList = CountryList
        self.keyName = keyName
        # 不同国家对应的目录文件
        self.CountryConfig = {
            "zh": "values-zh-rCN",
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

    def getXML(self,Country):
        # 使用minidom解析器打开 XML 文档
        file = "res/%s/strings.xml" % self.CountryConfig.get(Country)
        DOMTree = xml.dom.minidom.parse(file)
        collection = DOMTree.documentElement

        # 在集合中key
        content = collection.getElementsByTagName("string")
        return content

    def getXMLValue(self,content):
        for item in content:
            if self.keyName == item.getAttribute("name"):
                try:
                    return item.childNodes[0].data
                except Exception as e:
                    return None

    def getAllXMLValue(self,testPrint=None):
        valueList = []
        for country in self.CountryList:
            content = self.getXML(country)
            value = self.getXMLValue(content)
            if testPrint:
                print(country, ":    ", value)
            valueList.append(value)
        return valueList


if __name__ == "__main__":

    #   获取单个key的 所有国家值
    name = "only_single_file_can_be_shared"
    print("key: %s"%name)

    readAllXML = doAllXML(CountryList,name)
    readAllXML.getAllXMLValue(1)


