from flask import Flask, render_template
from flask_restx import Api
from app.setup_db import db
from app.config import Config
from app.views.genre import genres_ns
from app.views.movie import movies_ns
from app.views.director import directors_ns
from app.views.auth import auth_ns
from app.views.user import user_ns

api = Api(title="Flask Course Project 3", doc="/docs")



def create_app(config_entity: Config) -> Flask:
    application = Flask(__name__)
    application.config.from_object(config_entity)

    @application.route('/')
    def index():
        return render_template('index.html')
    register_extensions(application)
    return application


def register_extensions(application: Flask):
    db.init_app(application)
    api.init_app(application)
    api.add_namespace(genres_ns)
    api.add_namespace(movies_ns)
    api.add_namespace(directors_ns)
    api.add_namespace(auth_ns)
    api.add_namespace(user_ns)


config = Config()
app = create_app(config)

if __name__ == '__main__':
    app.run(port=25000)
