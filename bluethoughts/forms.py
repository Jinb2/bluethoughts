from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired,Length

class PostForm(FlaskForm):
    keywords = StringField('keywords',validators=[DataRequired(), Length(min=3,max=16)])

    message = TextAreaField('message', validators=[DataRequired()])

    location = StringField('location',validators=[DataRequired(), Length(max=16)])

    submit = SubmitField('Post your thoughts')
