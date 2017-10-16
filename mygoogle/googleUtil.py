#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017-10-16

@author: Administrator
'''

import urllib2
print '谷歌'


def obtainGoogleResult(wd):
    '''去请求谷歌
    https://www.google.com/search?q=baidu
    '''
    realUrl = 'https://www.google.com/search?q={wd}'.format(wd = wd)
    realResText = '谷歌'
    print realUrl
    req = urllib2.Request(realUrl)
    headerInfo = '''Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'''
    req.add_header('User-Agent',headerInfo)
    realResText = urllib2.urlopen(req).read()
#     soup = BeautifulSoup(realResText)
#     print type(soup)
    print realResText
    return realResText