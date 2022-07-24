from app.setup_db import db
from marshmallow import Schema, fields


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    #favorite_genre = db.Column(db.String(100))


class UserSchema(Schema):
    # атрибут password убран из схемы сериализации по соображениям инфосека
    id = fields.Int()
    email = fields.Str()
    name = fields.Str()
    surname = fields.Str()
    #favorite_genre = fields.Str()
