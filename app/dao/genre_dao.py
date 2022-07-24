from app.constants import PAGE_SIZE
from app.dao.models.genre import Genre


class GenreDAO:
    def __init__(self, db_session):
        self.session = db_session

    def get_one(self, pk: int):
        return self.session.query(Genre).get(pk)

    def get_all(self, request_args: dict):
        '''Функция возвращает все записи.
        При этом если в теле запроса есть поле status, со значением
        new, возвращаем записи в отсортированном виде.
        Кроме того, реализована пагинация (отсчёт страниц начинается с 1)
        '''

        query = self.session.query(Genre)

        if request_args.get("status") == 'new':
            query = query.order_by(Genre.id.desc())

        if request_args.get("page"):
            page = request_args.get("page")
            query = query.limit(PAGE_SIZE).offset((page - 1) * PAGE_SIZE)

        return query.all()

    def create(self, g_data: dict):
        genre = Genre(**g_data)
        self.session.add(genre)
        self.session.commit()
        return genre

    def delete(self, pk: int):
        genre = self.get_one(pk)
        self.session.delete(genre)
        self.session.commit()

    def update(self, genre_entity_upd: Genre):
        self.session.add(genre_entity_upd)
        self.session.commit()
