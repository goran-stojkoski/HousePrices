from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class QueryForm(FlaskForm):
    suburb = StringField('Suburb',validators=[DataRequired()])
    submit = SubmitField('Search')