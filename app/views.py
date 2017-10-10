#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-10 11:32:24
# @Author  : FZQ
# @Link    : http://example.org
# @Version : $v1.0$

from app import app
from flask import render_template
from app.models import Todo

@app.route('/')
def index():
	todos = Todo.objects.all()
	return render_template("index.html", todos=todos)
