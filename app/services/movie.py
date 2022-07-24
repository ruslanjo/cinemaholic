from app.dao.movie_dao import MovieDAO


class MovieService:
    def __init__(self, movie_dao: MovieDAO):
        self.dao = movie_dao

    def get_one(self, pk: int):
        return self.dao.get_one(pk)

    def get_all(self, request_args):
        return self.dao.get_all(request_args)

    def create(self, movie_data: dict):
        return self.dao.create(movie_data)

    def delete(self, pk: int):
        self.dao.delete(pk)

    def update(self, movie_data: dict):
        movie = self.dao.get_one(movie_data.get("pk"))
        movie.title = movie.get("title")
        movie.description = movie.get("description")
        movie.trailer = movie.get("trailer")
        movie.year = movie.get("year")
        movie.rating = movie.get("rating")
        movie.genre_id = movie.get("genre_id")
        movie.director_id = movie.get("director_id")

        self.dao.update(movie)

    def update_partial(self, movie_data: dict):
        movie = self.get_one(movie_data.get("pk"))

        if "title" in movie_data:
            movie.title = movie_data.get("title")
        if "description" in movie_data:
            movie.description = movie.get("description")
        if "trailer" in movie_data:
            movie.trailer = movie.get("trailer")
        if "year" in movie_data:
            movie.year = movie.get("year")
        if "rating" in movie_data:
            movie.rating = movie.get("rating")
        if "genre_id" in movie_data:
            movie.genre_id = movie.get("genre_id")
        if "director_id" in movie_data:
            movie.director_id = movie.get("director_id")

