from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    post = StringField('Название', validators=[DataRequired()])
    description = StringField('Описание', validators=[DataRequired()])
    picture = FileField('Фото', validators=[DataRequired()])

    submit = SubmitField('Подтвердить')
