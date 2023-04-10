from flask import Blueprint,render_template,request


# Defining a blueprint
index_page = Blueprint(
    'index', __name__,
    template_folder='templates',
    static_folder='static',
    static_url_path='')

@index_page.route('/')
def index():
    userAgent = request.headers.get('User_Agent').lower()
    return render_template('index.html')