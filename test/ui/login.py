#!/usr/bin/python
# -*- coding: UTF-8 -*-
from Tkinter import *
from tkMessageBox import *
import os

import sys
sys.path.append("/home/linux/python/test/fileandsql")

import text



class MyOneApplication(Frame):
    name, pwd =  None, None
    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.pack()
        self.__create_widgets()
        pass

     #创建登录时需要的控件

    def __create_widgets(self):
        x, y = self.get_window()

        self.header = Label(self, text = "对文件的操作", font = ("宋体", 15))
        self.header.pack()

        # self.la_name = Label(self, text = "账号",font=("宋体",32))     这里有问题无法控制  Label控件的大小...
        # # self.la_name.pack()
        # Label(self, text = "密码")

        self.user_name  = Entry(self)
        self.user_pwd = Entry(self, show = "*")

        # self.user_name.configure(width = w, height = h,state = "disabled")   无法在函数中销毁该视图   感觉是回调的问题

        self.btn_login = Button(self, text = "登录", width = 5, height = 1, command = self.__login)


        # self.header.place(x = 190, y = 150)
        # self.btn_login.place()
        self.user_name.pack()
        self.user_pwd.pack()
        self.btn_login.pack()
        pass

        #返回窗口的大小

    def get_window(self):
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = (ws / 2) - 200
        y = (hs / 2) - 200
        return x, y
        pass

    def __login(self):
        name = str(self.user_name.get())
        pwd = str(self.user_pwd.get())
        if name == "aaa" and pwd == "aaa":
            self.on_destroy()
            text.get_images()
            self.__run_image()
        else:
            self.select('您的输入不正确...', "输入错误...")

    def select(self, title, content):
        ask = askokcancel('askokcancel messagebox', title)
        if ask:
            print(content)
            pass
        pass

     #显示文件操作视图

    def __run_image(self):
        root_path = "/home/linux/python/image/"
        # img = Image.open(root_path + "0.jpg")
        # t = Text(self)
        # bm = BitmapImage("/home/linux/python/image/0.jpg")
        # t.image_create('1.0',image = bm)
        # t.pack()
        # self.text = Text(self).pack()  无法获取其中的text


        self.btn_save = Button(self, text = "删除", command = self.delete)
        self.lv = Listbox(self)
        self.btn_save.pack()

        list_path = text.get_images()

        for item in list_path:
            self.lv.insert(END, item)
            pass

        self.lv.pack()
        pass


    def delete(self):
        file_del = "/home/linux/python/image/" + self.lv.get(self.lv.curselection())
        if file_del == "/home/linux/python/image/{0}.jpg":
            self.select("无法删除...", "这是一个目录")

        os.remove(file_del)
        self.on_destroy()
        self.__run_image()
        pass

    #这里只是把根的控件对象销毁了  并未销毁根视图

    def on_destroy(self):
        for weight in self.winfo_children():
            weight.destroy()
            pass
        pass


app = MyOneApplication()
app.master.geometry("600x400")
app.master.title("欢迎进入我的第一个python程序...")
app.mainloop()
