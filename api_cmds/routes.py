from flask import render_template
from flask import Blueprint
from flask import request
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


@sign_up_page.route('/signup', methods=['GET', 'POST'])
def sign_up():

    # If the request method is POST, it means that the request has come from the clicking of the submit button
    if request.method == 'POST':
        return "Successfully submitted form"

    # Get request means this is a fresh request and is not coming from clicking the submit button
    form = SignUpForm()
    return render_template('sign_up.html', form=form)
