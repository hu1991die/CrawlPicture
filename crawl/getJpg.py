#coding=utf-8
# Created by feizi at 2016/3/9
import re
import urllib

import datetime


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    req = r'class="BDE_Image".*?src="(.+?\.jpg)"'
    imgre = re.compile(req)
    imglist = re.findall(imgre, html)
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, '%s.jpg' % x)
        x += 1

html = getHtml("http://tieba.baidu.com/p/997742003")

#开始时间
startTime = datetime.datetime.now()
print getImg(html)
#结束时间
endTime = datetime.datetime.now()
print '总共耗时：%s秒' % (endTime - startTime).seconds
