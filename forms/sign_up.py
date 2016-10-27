from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import PasswordField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import Email
from wtforms.validators import Length


class SignUpForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired('Please enter your first name')])
    last_name = StringField('Last Name', validators=[DataRequired('Please enter your last name')])
    email = StringField(
        'Email Address',
        validators=[
            DataRequired('Please enter your email address'),
            Email('Please enter a valid email address'),
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired('Please enter your password'),
            Length(min=6, message='Password needs to be a minimum of 6 characters'),
        ]
    )
    submit = SubmitField('Submit')