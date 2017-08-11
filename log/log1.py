#/usr/bin/env python
#coding=utf-8

import logging
# logging.__date__("%a,%y-%m-%d  %H:%M:%S")

logger = logging.getLogger()  #日志对象

logger.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s")


fh = logging.FileHandler('test1.log')      #日志处理对象，表示文件输出
ch = logging.StreamHandler()     #日志处理对象，表示终端输出

fh.setFormatter(formatter)   #采用什么样的输出格式
ch.setFormatter(formatter)

#给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)


print dir(logging)

# logger.debug("debug message")
# logger.info("info message")
# logger.error("error message")
# logger.warning("warning message")
# logger.critical("critical message")
