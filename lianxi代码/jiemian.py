#!/usr/bin/python
#coding=utf-8

from Tkinter import *
from tkMessageBox import *

import os



class MyOneApplication(object):
    name, pwd = None, None
    def __init__(self, master = None):

        self.pack()
        self.__create_widgets()

        #创建
