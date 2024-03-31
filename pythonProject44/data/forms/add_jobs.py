from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    post = StringField('Название', validators=[DataRequired()])
    author = IntegerField('Автор', validators=[DataRequired()])
    description = StringField('Описание', validators=[DataRequired()])
    is_finished = BooleanField('Пост актуален?')

    submit = SubmitField('Подтвердить')
