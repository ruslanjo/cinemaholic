from flask import abort
import base64
import jwt
import datetime
import calendar
import hmac
import hashlib
from app.constants import HASH_NAME, SALT, ITERATIONS, SECRET, JWT_ALGO
from app.dao.user_dao import UserDAO
from app.helpers.utils import compare_passwords


class AuthService:
    def __init__(self, user_dao: UserDAO):
        self.dao = user_dao

    def generate_token(self, data: dict, token_lifetime_minutes: int):
        token_lifetime = datetime.datetime.utcnow() + datetime.timedelta(minutes=token_lifetime_minutes)
        data["exp"] = calendar.timegm(token_lifetime.timetuple())

        token = jwt.encode(payload=data, key=SECRET, algorithm=JWT_ALGO)
        return token

    def return_tokens(self, data: dict, is_refresh=False):
        # Если первичная генерация токена, то нужно проверить пароль
        # если же это получение рефреш токента, то мы можем доверять и не будем проверять пароль

        email = data.get('email')
        password = data.get('password')

        user = self.dao.get_one_by_email(email)

        if not is_refresh:
            # Аутентифицируем пользователя
            if not compare_passwords(password, user.password):
                abort(400)

        access_token = self.generate_token(data, 30)
        refresh_token = self.generate_token(data, 130)

        return {"access_token": access_token, "refresh_token": refresh_token}

    def update_tokens(self, refresh_token):
        # если рефреш токен действителен и валиден, то генерируем новую пару access-refresh
        try:
            data = jwt.decode(refresh_token, SECRET, algorithms=[JWT_ALGO])
        except jwt.DecodeError:
            abort(400, 'access denied')
        else:
            return self.return_tokens(data, is_refresh=True)





