
# multilanguageautotest
#### Author: Wechat_Benjamin

##

## 简介
开发工具的初衷为的解决日常重复而繁琐的提高验证速度，多语言验证字符串准确性验证，普遍操作是一次操作看 5、6 部手机每部手机切换不同语言对比验证。

移动端产品出海后随着产品功能迭代，功能随之加多需要验证的多语言文案逐渐增多，测试验证文案对比耗时也越来越长。如：产品支持10余个国家平均产品文案200-300行左右，意味着需要验证的String文案有2000-3000的点对比这是一项非常繁琐而又耗时的工作，耗时长且容易漏掉。

多语言不认识的情况人工仅核对头尾符合然后再逐一标记其正确性，再检查 UI 超边界显示齐全的问题这算比较常规的操作。若中途开发有修改或新增某几处多语言时又要重新操作，耗时耗力。

### Python 一键查询 key 或模糊匹配 GUI 工具

一款支持 apk 反编译资源目录后快速验证多个国家 string.xml 的语言配置工具，国家顺序和国家配置可灵活配置，同时查询支持 Key 和 模糊 两种方式查询。

### Python 多语言自动化验证并生成Excel报告工具

根据Excel多语言表格，开发更新APK应用多语言string.xml配置。程序获取APK应用多语言文件配置并和产品规定Excel文档自动对比验证并进行颜色标记生成报告

##

## 文件目录说明 

#### 1、apktool 反编译环境依赖


#### 2、apktoolTest 反编译APK应用res资源文件夹多语言string.xml配置


#### 3、MultilingualTest 单key和模糊查询;多语言单key和关键字模糊搜索，Exlce表格和string.xml字符串自动化对比并生成报告；

#### 4、ImageDemo 项目演示截图

##

## 项目exe文件说明


### ../apktoolTest/testGUI.exe


#### 反编译apk工具，需要apktool环境依赖
#### 详细介绍：https://blog.csdn.net/qq_25305833/article/details/108540552



### ../MultilingualTest/dist/testOneGUI.exe


#### 资源读取工具：
#### 1、支持单个key查询
#### 2、支持字符串模糊匹配
#### 详细介绍：https://blog.csdn.net/qq_25305833/article/details/108540840


### ../MultilingualTest/dist/testReadExcleGUI.exe


#### 表格处理工具，支持exlce表格读取，string.xml支持多语言国家配置读取，最后进行数据对比标记存储到指定的exlce表格中并生成报告文件
#### 详细介绍：https://blog.csdn.net/qq_25305833/article/details/105867809

##

## 实现原理说明

1、反编译APK应用res资源文件夹多语言string.xml配置，详细请看CSDN文字描述

2、获取res文件夹中的不同国家的配置文件，并解析xml文件按照 { Key：Value } 的形式解析

3、多语言单key查询，实现是根据配置的不同国家先后顺序，遍历获取不同国家的Value值并打印显示出对应国家多语言

4、关键字模糊搜索，利用搜索的“倒排”，如果Value中包含搜索的关键字则获取该Key，获取到队列Key，再重复步骤3依次打印显示

5、Excel多语言自动化测试报告，读取表格key列的列表，通过Key获取实际的Value值，并对Excel中的国家Value值对比并对验证接口标记颜色（红色、绿色、黄色）

##
