from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class JobForm(FlaskForm):
    job = StringField('Название', validators=[DataRequired()])
    team_leader = IntegerField('Описание', validators=[DataRequired()])
    work_size = StringField('Прикрепить фото / видео', validators=[DataRequired()])
    collaborators = StringField('Collaborators', validators=[DataRequired()])
    is_finished = BooleanField('Пост актуален?')

    submit = SubmitField('Подтвердить')
