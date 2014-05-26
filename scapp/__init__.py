#!/usr/bin/env python
#coding=utf-8
import sys

reload(sys)  
sys.setdefaultencoding('utf8')

from flask import Flask, render_template,flash
from flask.ext.login import LoginManager
#import ibm_db_sa.ibm_db_sa

# 初始化
app = Flask(__name__)

# 读取配置文件
#app.config.from_object('scapp.config.DevConfig') # sqlite
app.config.from_object('scapp.config.ProConfig') # mysql

# 404错误跳转
@app.errorhandler(404)
def page_not_found(error):
    return render_template('errors/404.html', error = error), 404
	
# 500错误跳转
@app.errorhandler(500)
def page_not_found(error):
    return render_template('errors/500.html', error = error), 500
    
#---------------------------------
#加载试图--johnny 放在最后防止循环引用
#---------------------------------
import views.index
