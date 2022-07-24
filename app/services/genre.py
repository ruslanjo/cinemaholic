from app.dao.genre_dao import GenreDAO


class GenreService:
    def __init__(self, genre_dao: GenreDAO):
        self.dao = genre_dao

    def get_one(self, pk: int):
        return self.dao.get_one(pk)

    def get_all(self, request_args):
        return self.dao.get_all(request_args)

    def create(self, g_data: dict):
        genre = self.dao.create(g_data)
        return genre

    def update(self, g_data):
        genre = self.get_one(g_data.get("pk"))
        genre.name = g_data.get("name")

        self.dao.update(genre)

    def delete(self, pk):
        self.dao.delete(pk)

