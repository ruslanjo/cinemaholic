from app.dao.director_dao import DirectorDAO


class DirectorService:
    def __init__(self, director_dao: DirectorDAO):
        self.dao = director_dao

    def get_one(self, pk: int):
        return self.dao.get_one(pk)

    def get_all(self, request_args):
        return self.dao.get_all(request_args)

    def create(self, d_data: dict):
        return self.dao.create(d_data)

    def delete(self, pk: int):
        self.dao.delete(pk)

    def update(self, d_data: dict):
        director = self.get_one(d_data.get("pk"))
        self.dao.update(director)
