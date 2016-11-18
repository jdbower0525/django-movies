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


def rater_listing(request):
    raters = models.Rater.objects.all()
    return render(request, 'rater_listing.html', {'raters': raters})


def rater_detail(request, d):
    rater = models.Rater.objects.get(pk=d)
    all_ratings = rater.rating_set.order_by("-rating")
    # movie = models.Movie.objects.get(pk=all_ratings.movie_id)
    return render(request, 'rater_detail.html',
                  {'rater': rater, 'all_ratings': all_ratings})
