# # -*- coding: UTF-8 -*-
import os
import sys
sys.path.append("/home/linux/python/test/intentdata")
# sys.path.append("/home/linux/study/python/day/test/ui")

import getImage
# import login
# from pathlib import Path
# import media
"""
    所有文件的操作
"""
dir = "/home/linux/python/image"
# def del_file(path , getName):
#     # root:目录的路径  dirs: 所有的目录   files: 所有的文件名
#     for root, dirs, files in os.walk(path):   #os.walk(path) 从path目录下获取所有的文件与目录
#         for name in files:
#             print(name)
# def write_path(wPath):
#     user_need_path = str(input("please write you need file name or other:"))
#     if user_need_path == "":
#         write_path()
#     else:
#         del_file(wPath, user_need_path)
# PurePath("/home/linux/python")
# ------------------------------------------------->
#    获取 ".jpg" 图片
def get_images():
    image_array = []
    for image in os.listdir(dir):
        if os.path.splitext(image)[1] == ".jpg":
            image_array.append(image)
    i = is_null(image_array)
    if i == 0:
        get_images()
    elif i == 1:
        return image_array
    pass

def is_null(list_path):
    size = len(list_path)
    if size == 0:
        getImage.get_image(getImage.get_html())
        return 0
    else:
        return 1
        pass

    pass


if __name__ == "__main__":
    # write_path(dir)
    get_images(dir)
    pass
