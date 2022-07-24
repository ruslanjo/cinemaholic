from app.constants import PAGE_SIZE
from app.dao.models.user import User


class UserDAO:
    def __init__(self, db_session):
        self.session = db_session

    def get_one(self, pk: int):
        return self.session.query(User).get(pk)

    def get_one_by_email(self, email: str):
        return self.session.query(User).filter(User.email == email).first()

    def get_all(self, request_args: dict):
        '''Функция возвращает все записи.
        При этом если в теле запроса есть поле status, со значением
        new, возвращаем записи в отсортированном виде.
        Кроме того, реализована пагинация (отсчёт страниц начинается с 1)
        '''

        query = self.session.query(User)

        if request_args.get("status") == 'new':
            query = query.order_by(User.id.desc())

        if request_args.get("page"):
            page = request_args.get("page")
            query = query.limit(PAGE_SIZE).offset((page - 1) * PAGE_SIZE)

        return query.all()

    def create(self, user_data: dict):
        user = User(**user_data)
        self.session.add(user)
        self.session.commit()
        return user

    def update(self, user_entity_upd: User):
        self.session.add(user_entity_upd)
        self.session.commit()

    def delete(self, pk: int):
        user = self.get_one(pk)
        self.session.delete(user)
        self.session.commit()
