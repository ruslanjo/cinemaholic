from app.constants import PAGE_SIZE
from app.dao.models.director import Director


class DirectorDAO:
    def __init__(self, db_session):
        self.session = db_session

    def get_one(self, pk: int):
        return self.session.query(Director).get(pk)

    def get_all(self, request_args: dict):
        '''Функция возвращает все записи.
        При этом если в теле запроса есть поле status, со значением
        new, возвращаем записи в отсортированном виде.
        Кроме того, реализована пагинация (отсчёт страниц начинается с 1)
        '''

        query = self.session.query(Director)

        if request_args.get("status") == 'new':
            query = query.order_by(Director.id.desc())

        if request_args.get("page"):
            page = request_args.get("page")
            query = query.limit(PAGE_SIZE).offset((page - 1) * PAGE_SIZE)

        return query.all()

    def create(self, d_data: dict):
        director = Director(**d_data)
        self.session.add(director)
        self.session.commit()
        return director

    def delete(self, pk: int):
        director = self.get_one(pk)
        self.session.delete(director)
        self.session.commit()

    def update(self, director_entity_upd: Director):
        # a logic of update is implemented in the service layer
        self.session.add(director_entity_upd)
        self.session.commit()
