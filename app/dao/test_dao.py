from app.dao.models.movie import Movie
from main import create_app
from app.config import Config
from app.setup_db import db
from app.dao.models.movie import MovieSchema


with create_app(Config()).app_context():
    data = db.session.query(Movie).first()
    print(MovieSchema().dump(data))
    #dao = MovieDAO(db.session)
    #print(dao.get_all( {"status": "new", "page":2}))
