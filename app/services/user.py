import base64
import hashlib
from flask import abort
from app.constants import HASH_NAME, SALT, ITERATIONS
from app.dao.user_dao import UserDAO
from app.helpers.utils import compare_passwords


class UserService:
    def __init__(self, user_dao: UserDAO):
        self.dao = user_dao

    def get_one(self, pk: int):
        return self.dao.get_one(pk)

    def get_one_by_email(self, email: str):
        return self.dao.get_one_by_email(email)

    def get_all(self, request_data: dict):
        return self.dao.get_all(request_data)

    def generate_hash(self, password: str):
        hashed_password = hashlib.pbkdf2_hmac(HASH_NAME,
                                              password.encode('utf-8'),
                                              SALT,
                                              ITERATIONS)

        return base64.b64encode(hashed_password)

    def create(self, request_data: dict):
        if ("email" and "password") not in request_data.keys():
            abort(400)

        password = request_data.get('password')
        request_data['password'] = self.generate_hash(password)

        return self.dao.create(request_data)

    def update(self, request_data: dict):
        user = self.dao.get_one(request_data.get('id'))

        #user.email = request_data.get('email')
        #user.password = self.generate_hash(request_data.get('password'))
        user.name = request_data.get('name')
        user.surname = request_data.get('surname')
        user.favorite_genre = request_data.get('favorite_genre')

        self.dao.update(user)

    def update_partial(self, request_data: dict):
        user = self.dao.get_one(request_data.get('id'))

        #if 'email' in request_data:
        #    user.email = request_data.get('email')
        existing_password = request_data.get('password_1')
        new_password = request_data.get('password_2')

        if compare_passwords(existing_password, user.password):
            user.password = self.generate_hash(new_password)
        else:
            abort(400, 'Wrong password')
        if 'name' in request_data:
            user.name = request_data.get('name')
        if 'surname' in request_data:
            user.surname = request_data.get('surname')
        if 'favorite_genre' in request_data:
            user.favorite_genre = request_data.get('favorite_genre')

        self.dao.update(user)

    def delete(self, pk: int):
        self.dao.delete(pk)


