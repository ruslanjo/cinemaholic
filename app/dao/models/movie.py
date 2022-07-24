from app.setup_db import db
from marshmallow import Schema, fields
from app.dao.models.director import Director, DirectorSchema
from app.dao.models.genre import Genre, GenreSchema


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    trailer = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
    genre = db.relationship('Genre', foreign_keys=[genre_id])  #, back_populates='movie', foreign_keys=[genre_id])
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'), nullable=False)
    director = db.relationship('Director', foreign_keys=[director_id])  #, back_populates='movie', foreign_keys=[director_id])


class MovieSchema(Schema):
    id = fields.Int()
    title = fields.Str()
    description = fields.Str()
    trailer = fields.Str()
    year = fields.Int()
    rating = fields.Float()
    genre = fields.Nested(GenreSchema)
    director = fields.Nested(DirectorSchema)
    #genre_id = fields.Int()
    #director_id = fields.Int()
