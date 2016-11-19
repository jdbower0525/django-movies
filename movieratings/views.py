from django.shortcuts import render
from ratingsapp import models



def accounts_profile(request, d):
    rater = models.User.objects.get(pk=d)
    all_ratings = rater.rating_set.order_by("-rating")
    # movie = models.Movie.objects.get(pk=all_ratings.movie_id)
    return render(request, 'profile.html',
                  {'rater': rater, 'all_ratings': all_ratings})
