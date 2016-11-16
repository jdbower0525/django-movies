from django.db import models

# Create your models here.


class Rater(models.Model):
    rater_age = models.IntegerField(default=0)
    rater_gender = models.CharField(max_length=1)
    rater_job = models.CharField(max_length=20)
    rater_zip = models.TextField(max_length= 10)

    def __repr__(self):
        return rater_id + ' ' + rater_age


class Movie(models.Model):
    movie_title = models.TextField(max_length=100)

    def __str__(self):
        return movie_title

# 196	242	3	881250949

class Rating(models.Model):
    user_id = models.IntegerField(default=0)
    movie_id = models.IntegerField(default=0)
    rating = models.FloatField(default=0)
    time_stamp = models.IntegerField(default=0)
#
# class Rating(models.Model):
#     user_id = models.ForeignKey(Rater)
#     movie_id = models.ForeignKey(Movie)
#     rating = models.IntegerField(default=0)
#     time_stamp = models.IntegerField(default=0)

    def __repr__(self):
        return rating
