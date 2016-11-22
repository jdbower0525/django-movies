from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login
from ratingsapp import models
from .models import Rating
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
    if request.method == "GET":
        user_form = UserForm()
        rater_form = RaterForm()
    elif request.method == "POST":
        user_form = UserForm(request.POST)
        rater_form = RaterForm(request.POST)
        if user_form.is_valid() and rater_form.is_valid():
            user = user_form.save
            rater = rater_form.save(commit=False)
            rater.user = user
            rater.save()
            login(request, user)
            password = user.password
            user.set_password(password)
            user.save()
            user = authenticate(username = user.username, password =password)
            login(request, user)
            return HttpResponseRedirect('/accounts/profile/')
    return render(request, 'create_user.html', {'user_form': user_form, 'rater_form': rater_form})


def profile(request):
    return render(request, 'profile.html')


def add_rating(request):
    if request.method == 'POST':
        form = RatingForm(request.POST)
        if form.is_valid():
            new_rating = RatingForm(request.POST)
            new_rating.save()
            return HttpResponseRedirect('/ratingsapp/accounts/profile/')
    else:
        form = RatingForm()
        return render(request, "add_rating.html", {'form': form})

# example
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
