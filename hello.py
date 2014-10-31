#!/usr/bin/env python
# coding=utf-8
from flask import Flask 
app=Flask(__name__)

@app.route('/')
def hello_world():
    return '<h>hello_world!</h>'

if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0')

