from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    post = StringField('Название', validators=[DataRequired()])
    author = StringField('Автор', validators=[DataRequired()])
    description = StringField('Описание', validators=[DataRequired()])
    picture = StringField('Фото', validators=[DataRequired()])

    submit = SubmitField('Подтвердить')
