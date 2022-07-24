from flask_restx import Namespace, Resource
from flask import request
from app.container import genre_service, genre_schema, genres_schema

genres_ns = Namespace('genres')

@genres_ns.route('/')
class GenresView(Resource):
    def get(self):
        request_args = request.args
        genres = genre_service.get_all(request_args)
        res = genres_schema.dump(genres)
        return res, 200

    def post(self):
        req_data = request.data
        genre_service.create(req_data)
        return req_data, 201

    def put(self):
        req_data = request.data
        genre_service.update(req_data)


@genres_ns.route('/<int:pk>/')
class GenreView(Resource):
    def get(self, pk):
        genre = genre_service.get_one(pk)
        return genre_schema.dump(genre), 200

    def delete(self, pk):
        genre_service.delete(pk)
        return '', 204
