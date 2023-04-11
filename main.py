from flask import Flask
from routes.index import index_page
from routes.news import news_page

UPLOAD_FOLDER = 'upload'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = b'_5#33434GTDFDFDFGGffsdfdsKijoQ8z\n\xec]/'

app.register_blueprint(index_page)
app.register_blueprint(news_page)