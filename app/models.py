#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-10 11:32:24
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

from app import db
import datetime

class Todo(db.Document):
    content = db.StringField(required=True, max_length=20)
    time = db.DateTimeField(default=datetime.datetime.now())
    status = db.IntField(default=0)