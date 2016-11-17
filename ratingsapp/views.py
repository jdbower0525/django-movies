from django.shortcuts import render
from django.http import HttpResponse
from ratingsapp import models


def index(request):
    return HttpResponse("Hello, you're at the ratings app index.")


def movie_listing(request):
    movies = models.Movie.objects.all()
    return render(request, 'movie_listing.html', {'movies': movies})


def movie_detail(request, d):
    movie = models.Movie.objects.get(pk=d)
    return render(request, 'movie_detail.html', {'movie': movie})
