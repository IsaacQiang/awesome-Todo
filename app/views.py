#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-10 11:32:24
# @Author  : FZQ
# @Link    : http://example.org
# @Version : $v1.0$

from app import app
from flask import render_template,request
from app.models import Todo

@app.route('/')
def index():
	todos = Todo.objects.all()
	return render_template("index.html", todos=todos)

@app.route('/add', methods=['POST',])
def add():
	content = request.form.get("content")
	todo = Todo(content=content)
	todo.save()
	todos = Todo.objects.all()
	return render_template("index.html", todos=todos)
@app.route('/done/<string:todo_id>')
def done(todo_id):
	todo = Todo.objects.get_or_404(id=todo_id)
	todo.status = 1
	todo.save()
	todos = Todo.objects.all()
	return render_template("index.html", todos=todos)

@app.route('/undone/<string:todo_id>')
def undone(todo_id):
	todo = Todo.objects.get_or_404(id=todo_id)
	todo.status = 0
	todo.save()
	todos = Todo.objects.all()
	return render_template("index.html", todos=todos)


