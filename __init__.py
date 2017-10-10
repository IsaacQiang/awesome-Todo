#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-10 11:32:24
# @Author  : FZQ
# @Link    : http://example.org
# @Version : $v1.0$

from flask import Flask

app = Flask(__name__)
app.config.from_object("config")

#from app import views, models