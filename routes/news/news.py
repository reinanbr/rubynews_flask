from flask import Blueprint,render_template,request,session, redirect,url_for,flash, send_from_directory
from flask import jsonify
from json import dump

from urllib.parse import quote
from random import choice
import datetime as dt
import os
import time


# Defining a blueprint
news_page = Blueprint(
    'news', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='')

@news_page.route('/news')
def index():
    userAgent = request.headers.get('User_Agent').lower()
    return render_template('news.html')