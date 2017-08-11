#!/usr/bin/python
#coding=utf-8
import re

str = """Django has a lot of documentation. A high-level overview of how it’s organized will help you know where to look for certain things:Tutorials takeyou by the hand through a series of steps to create a Web application. Start here if you’re new to Django or Web application development. Also look at the “First steps” below.\
    Topic guides discuss key topics and concepts at a fairly high level and provide useful background information and explanation.\
    Reference guides contain technical reference for APIs and other aspects of Django’s machinery. They describe how it works and how to use it but assume that you have a basic understanding of key concepts.\
    How-to guides are recipes. They guide you through the steps involved in addressing key problems and use-cases. They are more advanced than tutorials and assume some knowledge of how Django works.\
"""


l = re.compile(r'(\w*)Django(\w*)')
k = l.findall(str)
print l
# print type(k),type(str),type(l)
# for value in k:
#     print value[0] + "Django" + value[1]
print k
