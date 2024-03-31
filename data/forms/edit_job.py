from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField, FileField
from wtforms.validators import DataRequired


class EditForm(FlaskForm):
    post = StringField('Название', validators=[DataRequired()])
    description = StringField('Описание', validators=[DataRequired()])

    submit = SubmitField('Подтвердить')