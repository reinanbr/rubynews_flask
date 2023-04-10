from flask import Flask
from routes.index import index_page
from routes.news import news_page


app = Flask(__name__)


app.register_blueprint(index_page)
app.register_blueprint(news_page)