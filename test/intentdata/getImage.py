#coding=utf-8
import urllib
import re
import os
"""
   网络获取图片
"""
# url = """https://cn.bing.com/images/search?q=%e4%b8%ad%e5%9b%bd%e6%96%b0%e5%9
#          e%8b%e5%8d%a7%e9%93%ba%e5%8a%a8%e8%bd%a6%e7%bb%84%e4%b8%8a%e7%ba%bf%e8,
#          %bf%90%e8%90%a5&FORM=ISTRTH&id=1FE0467BD7CD64FCF8DDEDAD5D5BD30C9DD86,
#          4B4&cat=%E4%BB%8A%E6%97%A5%E7%83%AD%E5%9B%BE&lpversion="""
imagePth = "/home/linux/python/test/image/{0}.jpg"
url = "https://tieba.baidu.com/p/2460150866"
# 获取整个页面

def get_html():
    page = urllib.urlopen(url)
    html = page.read()
    return html

#获取图片所有地址

def get_image(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    if os.path.exists(imagePth):
        installImg(imglist)
    else:
        os.makedirs(imagePth)
        installImg(imglist)
    pass

#保存图片到本地

def installImg(list):
    x = 0
    for imageUrl in list:
        try:
            #再次执行时....这里会把默认下载好的图片重新下载
            urllib.urlretrieve(imageUrl,imagePth.format(x))   #该方法的参数链表...
            pass
        except Exception as e:
            print("图片下载失败...")
            raise
        finally:
            print("图片%d结束..."%x)
            pass
        x = x + 1
# print("下载成功...")

if __name__ == "__main__":
    html = get_html()
    get_image(html)
