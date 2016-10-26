from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField


class SignUpForm(Form):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('Email Address')
    password = PasswordField('Password')
    submit = SubmitField('Submit')