#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017-10-16

@author: Administrator
'''
import urllib2
print '百度'


def obtainBaiduResult(wd):
    '''去请求百度'''
    realUrl = 'https://www.baidu.com/s?wd={wd}'.format(wd = wd)
    realResText = '百度'
    print realUrl
    req = urllib2.Request(realUrl)
    headerInfo = '''Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'''
    req.add_header('User-Agent',headerInfo)
    realResText = urllib2.urlopen(req).read()
#     soup = BeautifulSoup(realResText)
#     print type(soup)
#     print realResText
    return realResText