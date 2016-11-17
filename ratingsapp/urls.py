from django.conf.urls import url
from . import views
import ratingsapp

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url((r'^movie/([0-9]+)'), ratingsapp.views.movie_detail, name='movie_detail'),
    url((r'^movie_listing$'), ratingsapp.views.movie_listing, name='movie_listing')
]
