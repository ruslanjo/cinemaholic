import json

from flask_restx import Namespace, Resource
from flask import request, abort, jsonify, make_response
from app.container import auth_service, user_service, user_schema

auth_ns = Namespace('auth')


@auth_ns.route('/register/')
class RegistrationView(Resource):
    def post(self):
        data = request.json
        user_service.create(data)
        return "", 201


@auth_ns.route('/login/')
class LoginView(Resource):
    def post(self):
        data = request.json

        if ('email' and 'password') not in data:
            abort(400)

        tokens = auth_service.return_tokens(data)

        return make_response(jsonify(tokens),
                             201)

    def put(self):
        data = request.json

        refresh_token = data.get('refresh_token')
        if refresh_token is None:
            abort(400)

        tokens = auth_service.update_tokens(refresh_token)

        return make_response(jsonify(tokens),
                             201)






