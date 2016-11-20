from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login
from ratingsapp.models import *
from django.db.models import Avg
from django.views import generic
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf.urls import include
from ratingsapp.forms import UserForm, RaterForm, LoginForm, RatingForm
from django.contrib.auth.models import User


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
    return render(request, 'rater_detail.html',
                  {'rater': rater, 'all_ratings': all_ratings})


def top_20(request):
    avg_list = models.Movie.objects.annotate(
            avg_rating=Avg('rating__rating')).order_by('-avg_rating')[:20]
    return render(request, 'top_20.html', {'avg_list': avg_list})


def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(**form.cleaned_data)
            login(request, user)
            return HttpResponseRedirect('/accounts/profile/')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})


def profile(request):
    return render(request, 'profile.html')


def add_rating(request):
    user = request.user
    rater = user.rater
    form = RatingForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            rater = user
            new_movie = form.cleaned_data['movie']
            new_rating = form.cleaned_data['rating']
            timestamp = 5
            new_rating = Rating.object.create(rater=rater,
                                              movie=new_movie,
                                              rating=new_rating,
                                              timestamp=timestamp
                                              )
            new_rating.save()
    return render(request, "add_rating.html")
### example
# def add_dinner(request):
#     if request.method == 'POST':
#         form = DinnerForm(request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['name']
#             text = form.cleaned_data['text']
#             diner = Dinner.objects.create(
#                             name = name,
#                             text = text,)


def view_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/ratingsapp/profile')
        else:
            return render(request, "login.html",
                          {"failed": True, "username": username})
    else:
        user_form = LoginForm()
        return render(request, "login.html", {'form': user_form})
#
# auths = Author.objects.order_by('-score')[:30]
# ordered = sorted(auths, key=operator.attrgetter('last_name'))
