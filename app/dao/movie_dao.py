#from app.config import Config
from app.constants import PAGE_SIZE
from app.dao.models.movie import Movie
#from app.main import create_app


class MovieDAO:
    def __init__(self, db_session):
        self.session = db_session

    def get_one(self, pk: int):
        return self.session.query(Movie).get(pk)

    def get_all(self, request_args: dict):
        '''Функция возвращает все записи.
        При этом если в теле запроса есть поле status, со значением
        new, возвращаем записи в отсортированном виде.
        Кроме того, реализована пагинация (отсчёт страниц начинается с 1)
        '''

        query = self.session.query(Movie)

        if request_args.get("status") == 'new':
            query = query.order_by(Movie.id.desc())

        if request_args.get("page"):
            page = request_args.get("page")
            query = query.limit(PAGE_SIZE).offset((page - 1) * PAGE_SIZE)

        return query.all()

    def create(self, movie_data: dict):
        movie = Movie(**movie_data)
        self.session.add(movie)
        self.session.commit()
        return movie

    def delete(self, pk: int):
        movie = self.get_one(pk)
        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_entity_upd: Movie):
        # A logic of update's method is implemented in service layer
        self.session.add(movie_entity_upd)
        self.session.commit()


