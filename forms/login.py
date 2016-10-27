from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Email


class LoginForm(FlaskForm):
    email = StringField(
        'Email Address',
        validators=[
            DataRequired('Please enter your email address'),
            Email('Please enter a valid email address'),
        ]
    )
    password = PasswordField('Password', validators=[DataRequired('Please enter your password')])
    submit = SubmitField('Submit')