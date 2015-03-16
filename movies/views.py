from operator import itemgetter
import time
import jsonpickle
from django.http import HttpResponse
from django.shortcuts import render
from movies.application import ApplicationService

from movies.models import *
from datetime import date


def home(request):
    return render(request, "movies/home.html")


def get(request, start, count, xres, yres):

    rating = Rating(5, 2)
    movie = Movie("b0183321", "Burke and Hare", 5040, date(2010, 1, 1), Image("p01pfpbp"), "Dark comedy about the Edinburgh duo who provided cadavers for the medical establishment.")
    movie.rating = rating

    movies = [movie]  # ApplicationService().get_movies(start, count)
    data = [
        {
            "title": x.title,
            "duration": time.strftime('%H:%M', time.gmtime(x.duration)),
            "year": x.first_broadcast_date.year,
            "image": "http://ichef.bbci.co.uk/images/ic/{0}x{1}/{2}.jpg".format(xres, yres, x.image.pid),
            "rating": x.rating.vote_average,
            "votes": x.rating.vote_count,
            "synopsis": x.short_synopsis
        }
        for x in movies
    ]
    data.sort(key=itemgetter("rating"))
    return HttpResponse(jsonpickle.encode(data), content_type="application/json")