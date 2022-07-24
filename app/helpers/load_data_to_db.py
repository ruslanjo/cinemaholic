from app.config import Config
from main import create_app
from app.setup_db import db

from app.dao.models.genre import Genre
from app.dao.models.director import Director
from app.dao.models.movie import Movie

from app.helpers.utils import read_json
from app.constants import RAW_JSON_PATH


def commit_data_from_list_to_db(db_model, data: list) -> None:
    for element in data:
        if "pk" in element.keys():
            del element["pk"]
        db.session.add(db_model(**element))


if __name__ == '__main__':
    with create_app(Config()).app_context():
        db.drop_all()
        db.create_all()

        raw_data = read_json(RAW_JSON_PATH)
        movies = raw_data.get('movies')
        genres = raw_data.get('genres')
        directors = raw_data.get('directors')

        data = [movies, genres, directors]
        models = [Movie, Genre, Director]

        for table_name, model in zip(data, models):
            commit_data_from_list_to_db(model, table_name)

        db.session.commit()

print('Data loaded successfully')
