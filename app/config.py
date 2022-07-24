from app.constants import DATABASE_PATH


class Config:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{DATABASE_PATH}/movie.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
