from app import app
from flask import render_template, flash, redirect, request

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index(methods=['GET']):
    return render_template('index.html')


