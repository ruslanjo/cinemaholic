from flask import request, abort
from flask_restx import Namespace, Resource
from app.container import user_service, user_schema
from app.helpers.auth_decorators import auth_required
user_ns = Namespace('user')


@user_ns.route('/')
class UserView(Resource):
    @auth_required
    def get(self):
        data = request.json
        if 'id' in data:
            user = user_service.get_one(data.get('id'))
        elif 'email' in data:
            user = user_service.get_one_by_email(data.get('email'))
        else:
            abort(400)

        return user_schema.dump(user), 200

    @auth_required
    def patch(self):
        data = request.json
        user_service.update_partial(data)
        return '', 204


@user_ns.route('/password/')
class PasswordView(Resource):
    @auth_required
    def put(self):
        data = request.json
        if ("id" and "password_1" and "password_2") not in request.json:

            abort(400, 'id, existing password and new password are needed to change the password')

        else:
            user_service.update_partial(data)

        return '', 204







