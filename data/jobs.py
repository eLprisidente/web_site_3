import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Jobs(SqlAlchemyBase):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    post = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    author = sqlalchemy.Column(sqlalchemy.String,
                               sqlalchemy.ForeignKey("users.name"))
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    picture = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    user = orm.relationship('User')
