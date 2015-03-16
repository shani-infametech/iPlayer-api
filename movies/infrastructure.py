import jsonpickle
import urllib.request
import dateutil.parser
from leto import settings
from urllib.parse import quote_plus
from movies.models import Movie, Image, Rating


class MovieService:
    def __init__(self):
        self.url = settings.MOVIE_SERVICE_URL

    @staticmethod
    def parse_movies(dictionary):
        for x in dictionary["episodes"]:
            p = x["programme"]
            yield Movie(
                p["pid"],
                p["title"],
                p["duration"],
                dateutil.parser.parse(p["first_broadcast_date"]),
                Image(
                    p["image"]["pid"]
                ),
                p["short_synopsis"]
            )

    def get(self):
        response = urllib.request.urlopen(self.url)
        data = response.read()
        text = data.decode("utf-8")
        obj = jsonpickle.decode(text)
        movies = MovieService.parse_movies(obj)
        return movies


class RatingService:
    def __init__(self, api_key):
        self.url = settings.RATING_SERVICE_URL
        self.api_key = api_key

    @staticmethod
    def parse_rating(dictionary):
        x = dictionary["results"][0]
        return Rating(
            float(x["vote_average"]),
            int(x["vote_count"])
        )

    def get(self, movie):
        url = self.url.format(quote_plus(movie.title), self.api_key)
        response = urllib.request.urlopen(url)
        data = response.read()
        text = data.decode("utf-8")
        obj = jsonpickle.decode(text)
        rating = RatingService.parse_rating(obj)
        return rating
