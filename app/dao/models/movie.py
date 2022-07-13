from app.setup_db import db
from marshmallow import Schema, fields


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    trailer = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    rating = db.Column(db.Float, nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'), nullable=False)
    genre = db.relationship('Genre', back_populates='movie', foreign_keys=[genre_id])
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'), nullable=False)
    director = db.relationship('Director', back_populates='movie', foreign_keys=[director_id])


