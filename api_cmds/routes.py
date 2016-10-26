from flask import render_template
from flask import Blueprint
from forms. sign_up import SignUpForm


index_page = Blueprint('index', __name__, template_folder='templates')
about_page = Blueprint('about', __name__, template_folder='templates')
sign_up_page = Blueprint('sign_up', __name__, template_folder='templates')


@index_page.route('/')
def index():
    return render_template('index.html')


@about_page.route('/about')
def about():
    return render_template('about.html')


@sign_up_page.route('/signup')
def sign_up():
    form = SignUpForm()
    return render_template('sign_up.html', form=form)
