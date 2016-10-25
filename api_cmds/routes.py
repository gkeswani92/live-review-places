from flask import render_template
from flask import Blueprint


index_page = Blueprint('index', __name__, template_folder='templates')
about_page = Blueprint('about', __name__, template_folder='templates')


@index_page.route('/')
def index():
    return render_template('index.html')


@about_page.route('/about')
def about():
    return render_template('about.html')
