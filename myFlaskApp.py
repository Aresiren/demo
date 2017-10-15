#!/usr/bin/env python
# _*_coding:utf-8_*_
'''
Created on 2017-10-15

@author: Administrator
'''

from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
from flask import make_response

from werkzeug.contrib.cache import SimpleCache
from myWeixin import weixinCommon




app = Flask(__name__)
cache = SimpleCache()

@app.route('/')
def hello_flask():
    return 'hello flask!'

@app.route('/test', methods=['POST', 'GET'])
def test_path ():
    return 'test get path.'

@app.route('/get', methods=['GET'])
def test_get ():
    if request.method == 'GET':
        data = request.args
        print data
        return 'get 请求的参数{data}'.format(data = data)
    else:
        return '不是get 请求'

@app.route('/post', methods=['POST'])
def test_post ():
    if request.method == 'POST':
        data = request.form
        print data
    return 'post 请求'

@app.route('/cacheSet', methods=['GET','POST'])
def testCacheSet():
    print 'cache'
    if request.method == 'GET':
        data = request.args
        value = data.get('key','')
        print type(value)
        if value.strip()=="":
            value = 'aaaa'
        else:
            print value
        print value
    weixinCommon.setCache(cache, 'x', value)
    return 'cache test set'
    
@app.route('/cacheGet', methods=['GET','POST'])
def testCacheGet():
    print 'cache'
    varStr = weixinCommon.showCache(cache, 'x')
    print type(varStr),varStr
    return 'cache test get'

@app.route('/weixin/test', methods=['GET','POST'])
def weixinTest():
    print '+++start controller or action:{funcNam}+++'.format(funcNam = 'weixinTest')
    if request.method == 'GET':
        data = request.args
        print 'get请求参数:{d}'.format(d=data)
    elif request.method == 'POST':
#         request.form.get('myid')    #input
        data = request.form
        print 'post请求参数:{d}'.format(d=data)
    else:
        print '未知请求类型'
    f = open("douban2.txt", "r")
    varStr = f.read()
    print varStr
#     return 'weixin test'
    return varStr
#     f = open("douban2.txt", "r")#douban.txt  index.html
#     return make_response(str(f))


# if __name__ == '__main__':
#    app.run(debug=True)
