#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017-10-15

@author: Administrator
'''
print 'weixinCommon start'

def showCache(cache,key):
    print 'get cache'
    value = cache.get(key)
    return value

def setCache(cache,key,value):
    print 'set cache'
    cache.set(key, value, timeout=5 * 60)
    
    return key, value
    