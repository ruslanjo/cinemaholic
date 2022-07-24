from flask_restx import Resource, Namespace
from flask import request
from app.container import director_service, director_schema, directors_schema
from app.dao.models.director import DirectorSchema

directors_ns = Namespace('directors')


@directors_ns.route('/')
class DirectorsView(Resource):
    def get(self):
        request_args = request.args
        directors = director_service.get_all(request_args)
        return directors_schema.dump(directors), 200

    def post(self):
        req_data = request.data
        director_service.create(req_data)
        return req_data, 201


@directors_ns.route('/<int:pk>')
class DirectorView(Resource):
    def get(self, pk):
        director = director_service.get_one(pk)
        return director_schema.dump(director), 200

    def delete(self, pk):
        director_service.delete(pk)
        return '', 204

    def put(self):
        req_data = request.data
        director_service.update(req_data)
        return '', 204

