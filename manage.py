#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-10-10 11:32:24
# @Author  : FZQ
# @Link    : http://example.org
# @Version : $v1.0$

from flask.ext.script import Manager, Server
from app import app

manager = Manager(app)
manager.add_command("runserver", Server(host='127.0.0.1', port=5000, use_debugger=True))

if __name__ == '__main__':
	manager.run()