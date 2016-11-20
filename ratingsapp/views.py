from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from ratingsapp import models
from django.db.models import Avg
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf.urls import include


def index(request):
    return render(request, 'index.html')


def movie_listing(request):
    movies = models.Movie.objects.all()
    return render(request, 'movie_listing.html', {'movies': movies})


def movie_detail(request, d):
    movie = models.Movie.objects.get(pk=d)
    all_ratings = movie.rating_set.order_by("-rating")
    return render(request, 'movie_detail.html',
                  {'movie': movie, 'all_ratings': all_ratings})


def rater_listing(request):
    raters = models.Rater.objects.all()
    return render(request, 'rater_listing.html', {'raters': raters})


def rater_detail(request, d):
    rater = models.Rater.objects.get(pk=d)
    all_ratings = rater.rating_set.order_by("-rating")
    # movie = models.Movie.objects.get(pk=all_ratings.movie_id)
    return render(request, 'rater_detail.html',
                  {'rater': rater, 'all_ratings': all_ratings})


def top_20(request):
    avg_list = models.Movie.objects.annotate(
            avg_rating=Avg('rating__rating')).order_by('-avg_rating')[:20]
    return render(request, 'top_20.html', {'avg_list': avg_list})


#
# auths = Author.objects.order_by('-score')[:30]
# ordered = sorted(auths, key=operator.attrgetter('last_name'))
