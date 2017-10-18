#!/usr/bin/env python
#_*_coding:utf-8_*_
'''
Created on 2017-10-18

@author: Administrator
'''

from flask import render_template
from flask import request
from flask import make_response
from flask import Blueprint

print '微信 视图'
# profile = Blueprint('profile', __name__)

@main.route('/wechat/message',methods=['GET','POST'])
def doMessage():
    return 'message'
