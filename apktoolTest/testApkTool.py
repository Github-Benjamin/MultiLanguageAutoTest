#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Benjamin
# @Time   : 2020/9/9 23:20


import os
import subprocess
import time

def doCmd(adbcmd,times=0.25):
    print(adbcmd)
    child = subprocess.Popen(adbcmd, shell=True)
    time.sleep(times)
    child.kill()

def delFile(cmd):
    fileName = cmd.split(" ")[-1].rsplit(".apk",1)[0]
    rmFileName = "rd/s/q " + fileName
    doCmd(rmFileName,3)

def getApkToolCmd(fileName):
    apkToolCmd = "apktool d -f --no-src " + fileName
    return apkToolCmd

def getApkRes(fileName):
    delFile(fileName)
    apkToolCmd = getApkToolCmd(fileName)
    doCmd(apkToolCmd,30)

# 获取文件路径并删除多余文件
def delNoUseFile(fileName):
    # filePath,fileName = os.path.abspath(fileName).rsplit("\\",1)
    filePath = os.getcwd()
    getFilePathName = fileName.rsplit(".apk",1)[0]
    dirs = os.listdir( getFilePathName)
    for file in dirs:
        print(file)
        rmFilePath = filePath + "\\" + getFilePathName  + "\\"
        if "res" not in file:
            doCmd("rd/s/q " + rmFilePath + file)
            doCmd("del /f /a /q  " + rmFilePath + file)

# adbcmd = "CleanLite_2.0.0(v3)_release-signed.apk"
# # # getApkRes(adbcmd)
# # #
# delNoUseFile(adbcmd)


