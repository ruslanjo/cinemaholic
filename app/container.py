from app.setup_db import db

from app.dao.movie_dao import MovieDAO
from app.dao.genre_dao import GenreDAO
from app.dao.director_dao import DirectorDAO
from app.dao.user_dao import UserDAO

from app.services.movie import MovieService
from app.services.genre import GenreService
from app.services.director import DirectorService
from app.services.user import UserService
from app.services.auth import AuthService

from app.dao.models.movie import MovieSchema
from app.dao.models.genre import GenreSchema
from app.dao.models.director import DirectorSchema
from app.dao.models.user import UserSchema

movie_dao = MovieDAO(db.session)
movie_service = MovieService(movie_dao)
movie_schema = MovieSchema()
movies_schema = MovieSchema(many=True)

genre_dao = GenreDAO(db.session)
genre_service = GenreService(genre_dao)
genre_schema = GenreSchema()
genres_schema = GenreSchema(many=True)

director_dao = DirectorDAO(db.session)
director_service = DirectorService(director_dao)
director_schema = DirectorSchema()
directors_schema = DirectorSchema(many=True)

user_dao = UserDAO(db.session)
user_service = UserService(user_dao)
user_schema = UserSchema()
users_schema = UserSchema(many=True)

auth_service = AuthService(user_dao)
