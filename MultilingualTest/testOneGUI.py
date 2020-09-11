# -*- coding: utf-8 -*-
# @Time    : 2020/9/10 10:05 下午
# @Author  : Benjamin
# @File    : testOneGUI.py
# @Software: PyCharm


import oneTest
import datetime
import tkinter


def getNowTime():
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')


def do():

    print("\n")
    print(getNowTime(),"开始执行","\n")



    try:
        # adbcmd = "C:\\Users\\Benjamin\\Desktop\\python\\apktoolTest\\ludashi_home.apk"



        path = e1.get()
        CountryList = e2.get().split(" ")
        CountryConfig = eval(e3.get())
        key = e4.get()
        select = iv_default.get()

        if select == 1:
            readAllXML = oneTest.doAllXML(path,CountryList,CountryConfig,key)
            data = readAllXML.getAllXMLValue(1)
        else:
            readAllXML = oneTest.doAllXML(path, CountryList, CountryConfig, key)
            data = readAllXML.getSearchValue()

        e6.delete(1.0, tkinter.END)
        e6.insert(tkinter.END, data)

    except Exception as e:
        print("警告数据出错，执行失败，请检查录入格式是否正确。")
        print("do Error:",e)
        return

    finally:
        print()
        print(getNowTime(), "执行完毕\n")



root = tkinter.Tk()
root.resizable(0, 0)
root.title('多语言单Key搜索查询')


c = tkinter.Label(root,text="")
c.grid(row=0,column=1)

l = tkinter.Label(root,text = 'res目录名称:')
l.grid(row=1,column=1,sticky=tkinter.W)
e1 = tkinter.Entry(root)
e1.grid(row=1,column=2,sticky=tkinter.E)


l = tkinter.Label(root,text = '国家顺序:')
l.grid(row=2,column=1,sticky=tkinter.W)
e2Value = tkinter.StringVar()
e2Value.set(["zh","en","ar","hi","ru","vi","pt","th","in","zhTW","zhTW","fr","es"])
e2 = tkinter.Entry(root,textvariable=e2Value)
e2.grid(row=2,column=2,sticky=tkinter.E)


l = tkinter.Label(root,text = '国家配置:')
l.grid(row=3,column=1,sticky=tkinter.W)
e3Value = tkinter.StringVar()
e3Value.set({
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
        })
e3 = tkinter.Entry(root,textvariable=e3Value)
e3.grid(row=3,column=2,sticky=tkinter.E)


l = tkinter.Label(root,text = '搜索模式')
l.grid(row=4,column=1,sticky=tkinter.W)
iv_default = tkinter.IntVar()
rb_default1 = tkinter.Radiobutton(root, text='Key', value=1, variable=iv_default)
rb_default2 = tkinter.Radiobutton(root, text='模糊', value=2, variable=iv_default)
iv_default.set(1)
rb_default1.grid(row=4,column=2,sticky=tkinter.W)
rb_default2.grid(row=4,column=2,sticky=tkinter.E)



l = tkinter.Label(root,text = '搜索单Key:')
l.grid(row=5,column=1,sticky=tkinter.W)
e4 = tkinter.Entry(root)
e4.grid(row=5,column=2,sticky=tkinter.E)

b = tkinter.Button(root,text = '确认',command=do)
b.grid(row=5,column=3,sticky=tkinter.E)
l = tkinter.Label(root,text = '')
l.grid(row=5,column=4,sticky=tkinter.W)



l = tkinter.Label(root,text = '查询结果:')
l.grid(row=6,column=1,sticky=tkinter.W)
e6 = tkinter.Text(root, width=20, height=18)
e6.grid(row=6,column=2)


c = tkinter.Label(root,text="")
c.grid(row=7,column=0)

c = tkinter.Label(root,text="Author WeChat:")
c.grid(row=8,column=1)
c = tkinter.Label(root,text="WeChat_Benjamin")
c.grid(row=8,column=2)



root.mainloop()



