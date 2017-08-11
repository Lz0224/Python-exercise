#/usr/bin/env python
#coding=utf-8

import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = "%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s",
    datefmt = "%a,%y-%m-%d  %H:%M:%S",
    filename = "test.log",
    filemode = "a",
)


logging.debug("debug message")
logging.info("info message")
logging.error("error message")
logging.warning("warning message")
logging.critical("critical message")
