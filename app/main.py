from flask import Flask
from flask_restx import Api
from setup_db import db
from config import Config


def create_app(config_entity: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config_entity)
    register_extensions(application)
    return application


def register_extensions(application: Flask):
    db.init_app(application)
    # api = Api(application)
    # create_data(application, db)
    # api.add_namespace(None)


def create_data(application, database):
    with application.app_context():
        database.create_all()


config = Config()

if __name__ == '__main__':
    app = create_app(config)

    app.run(port=2034)

