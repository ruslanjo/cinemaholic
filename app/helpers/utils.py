import base64
import hashlib
import hmac
import json

from app.constants import HASH_NAME, SALT, ITERATIONS


def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def compare_passwords(given_password: str, password_from_db: bytes) -> bool:
    given_password_hashed = hashlib.pbkdf2_hmac(HASH_NAME,
                                                given_password.encode('utf-8'),
                                                SALT,
                                                ITERATIONS)

    db_password = base64.b64decode(password_from_db)

    return hmac.compare_digest(given_password_hashed, db_password)