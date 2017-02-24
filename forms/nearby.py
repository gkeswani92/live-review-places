from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import SubmitField
from wtforms.validators import DataRequired


class NearbySearchForm(FlaskForm):
    keyword_search = StringField('Keyword')
    address = StringField('Address', validators=[DataRequired("Please enter an address")])
    submit = SubmitField("Search")
