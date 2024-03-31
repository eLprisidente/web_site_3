from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class CommentForm(FlaskForm):
    comment = StringField('Комментарий', validators=[DataRequired()])

    submit = SubmitField('Подтвердить')
