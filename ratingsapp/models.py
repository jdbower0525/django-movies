from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
import datetime


class Rater(models.Model):
    rater_age = models.IntegerField(default=0)
    rater_gender = models.CharField(max_length=1)
    rater_job = models.CharField(max_length=20)
    rater_zip = models.TextField(max_length= 10)

    def __repr__(self):
        return rater_id + ' ' + rater_age


class Movie(models.Model):
    movie_title = models.TextField(max_length=100)

    @property
    def url(self):
        return reverse('movie_detail', args=[self.pk])


    def avg_rating(self):
        r_set = self.rating_set.all()
        if len(r_set) == 0:
            return 0
        else:
            dict = r_set.aggregate(Avg('rating'))
            return round(dict["rating__avg"], 2)


    def __str__(self):
        return movie_title

# annuals = models.ForeignKey(Annual, related_name='annuals_ordered', blank=True, null=True)

class Rating(models.Model):
    rater = models.ForeignKey(Rater, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField(default=0)
    time_stamp = models.IntegerField(default=0)

    def __repr__(self):
        return rating
