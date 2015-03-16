import time
import jsonpickle
from leto import settings
from operator import itemgetter
from django.http import HttpResponse
from django.shortcuts import render
from movies.application import ApplicationService


def home(request):
    return render(request, "movies/home.html")


def get(request, start, count, xres, yres):
    movies = ApplicationService(rating_api_key=settings.RATING_API_KEY).get_movies(int(start), int(count))
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