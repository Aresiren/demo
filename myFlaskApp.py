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
from flask import redirect,url_for

import urllib

from werkzeug.contrib.cache import SimpleCache
from myWeixin import weixinCommon
from mybaidu import baiduUtil
from mygoogle import googleUtil
# from . import main

import os
from flask import send_from_directory
import time
import hashlib
import xml.etree.ElementTree as ET


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
        return 'get 请求的参数{data}'.format(data=data)
    else:
        return '不是get 请求'

@app.route('/post', methods=['POST'])
def test_post ():
    if request.method == 'POST':
        data = request.form
        print data
    return 'post 请求'

@app.route('/cacheSet', methods=['GET', 'POST'])
def testCacheSet():
    print 'cache'
    if request.method == 'GET':
        data = request.args
        value = data.get('key', '')
        print type(value)
        if value.strip() == "":
            value = 'aaaa'
        else:
            print value
        print value
    weixinCommon.setCache(cache, 'x', value)
    return 'cache test set'
    
@app.route('/cacheGet', methods=['GET', 'POST'])
def testCacheGet():
    print 'cache'
    varStr = weixinCommon.showCache(cache, 'x')
    print type(varStr), varStr
    return 'cache test get'

@app.route('/weixin/test', methods=['GET', 'POST'])
def weixinTest():
    print '+++start controller or action:{funcNam}+++'.format(funcNam='weixinTest')
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

@app.route('/wechat/auth',methods=['GET','POST'])
def wechat_auth():
    if request.method == 'GET':
        print '/wechat/auth 微信认证'
        token='token1234Token' #微信配置所需的token
        data = request.args
        signature = data.get('signature','')
        timestamp = data.get('timestamp','')
        nonce = data.get('nonce','')
        echostr = data.get('echostr','')
        s = [timestamp,nonce,token]
        s.sort()
        s = ''.join(s)
        if (hashlib.sha1(s).hexdigest() == signature):
            return make_response(echostr)
    else:
        rec = request.stream.read()
        xml_rec = ET.fromstring(rec)
        tou = xml_rec.find('ToUserName').text
        fromu = xml_rec.find('FromUserName').text
        content = xml_rec.find('Content').text
        xml_rep = "<xml><ToUserName><![CDATA[%s]]></ToUserName><FromUserName><![CDATA[%s]]></FromUserName><CreateTime>%s</CreateTime><MsgType><![CDATA[text]]></MsgType><Content><![CDATA[%s]]></Content><FuncFlag>0</FuncFlag></xml>"
        response = make_response(xml_rep % (fromu,tou,str(int(time.time())), content))
        response.content_type='application/xml'
        return response
    return 'Hello weixin!'



@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
                               os.path.join(app.root_path, 'static'),
                               'favicon.ico', 
                               mimetype='image/vnd.microsoft.icon'
                               )
@app.route('/images/branding/googlelogo/2x/googlelogo_color_120x44dp.png')  
def googlelogo1():
    '''
    重定向请求(1)
    '''
    return send_from_directory(
                               os.path.join(app.root_path, 'static/images/branding/googlelogo/2x'),
                               'googlelogo_color_120x44dp.png', 
                               mimetype='image/vnd.microsoft.icon'
                               )

@app.route('/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png')  
def googlelogo2():
    '''
    重定向请求(2)
    '''
    return send_from_directory(
                               os.path.join(app.root_path, 'static/images/branding/googlelogo/1x'),
                               'googlelogo_color_272x92dp.png', 
                               mimetype='image/vnd.microsoft.icon'
                               )

#搜索引擎
#百度
@app.route('/baidu', methods=['GET'])
def doBaidu():
    print '百度搜索'
    htmlStr = render_template('baidu.html')
    return htmlStr

@app.route('/s', methods=['GET'])
def doBaidus():
    print ''
    wd = ''
    if request.method == 'GET':
        data = request.args
        print data
        wd = data.get('wd','').encode('utf-8')
        print wd
#     htmlStr = baiduUtil.obtainBaiduResult(wd)
#    urllib.quote(wd)-->URL编码
    htmlStr = baiduUtil.obtainBaiduResult(urllib.quote(wd))
    return htmlStr 

#谷歌
@app.route('/google', methods=['GET'])
def doGoogle():
    print '/google 谷歌搜索'
#     htmlStr = render_template('google.html')
#     f = open('templates/google.html','r')
#     f = open("douban2.txt", "r")
#     htmlStr = f.read()
#     return 'google'
    htmlStr = redirect(url_for('doGoogles'))#302 (测试doBaidu)(doGoogles) 将/google页面 重定向到 /search页面
    print '执行重定向...'
    return htmlStr

@app.route('/search', methods=['GET'])
def doGoogles():
    '''
    https://www.google.com/search?q=baidu
    '''
    print '/search'
    wd = ''
    if request.method == 'GET':
        data = request.args
        print data
        wd = data.get('q','').encode('utf-8')
        print wd
#     htmlStr = googleUtil.obtainGoogleResult(wd)
    #    urllib.quote(wd)-->URL编码
    htmlStr = googleUtil.obtainGoogleResult(urllib.quote(wd))
    return htmlStr

# if __name__ == '__main__':
#    app.run(debug=True)
