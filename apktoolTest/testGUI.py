#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author : Benjamin
# @Time   : 2020/9/9 23:23

import datetime
import testApkTool
import tkinter


def getNowTime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def do():
    print("\n")
    print(getNowTime(),"开始执行")

    try:
        # adbcmd = "C:\\Users\\Benjamin\\Desktop\\python\\apktoolTest\\ludashi_home.apk"
        adbcmd = e1.get()
        testApkTool.getApkRes(adbcmd)
        testApkTool.delNoUseFile(adbcmd)
        # testApkTool.getApkRes(e1.get())
    except Exception as e:
        print("警告数据出错，执行失败，请检查表格格式是否正确。")
        print("do Error:",e)
        return

    print(getNowTime(), "执行完毕\n")



root = tkinter.Tk()
root.resizable(0, 0)
root.title('回弹原始记录 表格自动化')

c = tkinter.Label(root,text="")
c.grid(row=0,column=0)

l = tkinter.Label(root,text = '文件名称:')
l.grid(row=1,column=1,sticky=tkinter.W)

e1 = tkinter.Entry(root)
e1.grid(row=1,column=2,sticky=tkinter.E)

b = tkinter.Button(root,text = '确认',command=do)
b.grid(row=1,column=3,sticky=tkinter.E)

l = tkinter.Label(root,text = '')
l.grid(row=1,column=4,sticky=tkinter.W)

c = tkinter.Label(root,text="")
c.grid(row=6,column=0)

root.mainloop()



