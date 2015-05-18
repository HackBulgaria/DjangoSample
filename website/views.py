from django.shortcuts import render
from .models import Movie


def index(request):
    movies = Movie.objects.all()

    return render(request, "index.html", locals())


def about(request):
    return render(request, "about.html")
