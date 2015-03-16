from movies.infrastructure import MovieService
from movies.infrastructure import RatingService


class ApplicationService:
    def __init__(self, movie_service=None, rating_service=None, rating_api_key=None):
        self.movie_service = movie_service if movie_service is not None else MovieService()
        self.rating_service = rating_service if rating_service is not None else RatingService(rating_api_key)

    def get_movies(self, start, count):
        movies = self.movie_service.get()
        for index, movie in enumerate(movies):
            if start <= index < start + count:
                movie.rating = self.rating_service.get(movie)
                yield movie