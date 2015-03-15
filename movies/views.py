from django.shortcuts import render


def home(request):
    data = {}
    return render(request, "movies/home.html", data)