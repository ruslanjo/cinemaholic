from flask import request
from flask_restx import Resource, Namespace
from app.container import movie_service, movie_schema, movies_schema

movies_ns = Namespace('movies')


@movies_ns.route('/')
class MoviesViews(Resource):
    def get(self):
        req_args = request.args
        movies = movie_service.get_all(req_args)
        return movies_schema.dump(movies), 200

    def post(self):
        req_data = request.data
        movie_service.create(req_data)
        return req_data, 201


@movies_ns.route('/<int:pk>/')
class MovieViews(Resource):
    def get(self, pk):
        movie = movie_service.get_one(pk)
        return movie_schema.dump(movie), 200

    def delete(self, pk):
        movie_service.delete(pk)
        return '', 204

    def put(self, pk):
        req_data = request.data
        movie_service.update(req_data)
        return '', 204

    def patch(self, pk):
        req_data = request.data
        movie_service.update_partial(req_data)
        return '', 204
