from flask import Blueprint,render_template,current_app,request,session,jsonify, redirect,url_for,flash, send_from_directory
from flask import jsonify
from json import dump
from werkzeug.utils import secure_filename

from .tools import upload_imgurl,save_news_

from urllib.parse import quote
from random import choice
import datetime as dt
import os
import time


dirname = os.path.dirname(os.path.abspath(__file__))

UPLOAD_FOLDER = dirname + "/upload"
ALLOWED_EXTENSIONS = ["png", "jpeg", "jpg"]
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# Defining a blueprint
news_page = Blueprint(
    'news', __name__,
    url_prefix='/news',
    template_folder='templates',
    static_folder='static',
    static_url_path='')

@news_page.route('/add_news')
def add_news():
    return render_template('add_news.html')


@news_page.route('/save_news',methods=['GET', 'POST'])
def save_news():
    if request.method=='POST':
        news = (request.form.get('news'))
        title = (request.form.get('title'))
        
        date = dt.datetime.now().strftime('%d/%m/%Y')
        hour = dt.datetime.now().strftime('%H:%M:%s')
        
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)

        file = request.files['file']
        if file and allowed_file(file.filename):
            namefile,ext = tuple(file.filename.split('.'))
            url_filename =  f'{quote(title)}.{ext}'
            filename = secure_filename(url_filename)
            print(UPLOAD_FOLDER,filename)
            path_file = os.path.join(UPLOAD_FOLDER, filename)
            file.save(path_file)
            
            upload_thumbnail = upload_imgurl(path_file,title)
            os.remove(path_file)
            
            news_db_ = {'title':title,
                       'news':news,
                       'date':{'date':date,'hour':hour,'time':time.time()},
                       'title_url':quote(title),
                       'thumbnail':{'link':upload_thumbnail.link,
                                    'title':upload_thumbnail.title}}
            print(news_db_)
            save_news_(news_db_)
  
            


    
    
    
    return jsonify({"sucess":"ok"})


@news_page.route('/')
def index():
    userAgent = request.headers.get('User_Agent').lower()
    return render_template('news.html')



