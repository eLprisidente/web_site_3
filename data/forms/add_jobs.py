from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    job = StringField('Название', validators=[DataRequired()])
    team_leader = StringField('Описание', validators=[DataRequired()])
    collaborators = StringField('Точка / Место', validators=[DataRequired()])
    is_finished = BooleanField('Пост актуален?')

    submit = SubmitField('Подтвердить')
