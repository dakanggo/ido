#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2024/11/15 18:08
# @Author  : DAKANG
# @File    : app.py
# @Software: PyCharm
from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
