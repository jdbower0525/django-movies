from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
import ratingsapp
from django.views.generic import TemplateView


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url((r'^movie/([0-9]+)'), ratingsapp.views.movie_detail,
        name='movie_detail'),
    url((r'^movie_listing$'), ratingsapp.views.movie_listing,
        name='movie_listing'),
    url((r'^rater/([0-9]+)'), ratingsapp.views.rater_detail,
        name='rater_detail'),
    url((r'^rater_listing$'), ratingsapp.views.rater_listing,
        name='rater_listing'),
    url((r'^top20$'), ratingsapp.views.top_20,
        name='top20'),
    url(r'^accounts/profile/$', ratingsapp.views.profile,
        name='user_profile'),
    url(r'^add_rating/$', ratingsapp.views.add_rating,
        name='add_rating'),
]
