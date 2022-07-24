from flask import request, abort
import jwt
from app.constants import JWT_ALGO, SECRET


def auth_required(func):
    def wrapper(*args, **kwargs):
        if "Authorization" not in request.headers:
            abort(401, 'unathorized')

        token = request.headers.get('Authorization')
        token = token.split('Bearer ')[-1]

        try:
            jwt.decode(token, SECRET, algorithms=[JWT_ALGO])

        except jwt.DecodeError as e:
            abort(401, str(e))

        return func(*args, **kwargs)
    return wrapper




