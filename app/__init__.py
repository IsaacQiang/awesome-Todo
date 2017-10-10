#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-10 11:32:24
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)
app.config.from_object("config")

db = MongoEngine(app)

from app import views, models