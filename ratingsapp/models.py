from django.db import models
from django.db.models import Avg
from django.urls import reverse


class Rater(models.Model):
    rater_age = models.IntegerField(default=0)
    rater_gender = models.CharField(max_length=1)
    rater_job = models.CharField(max_length=20)
    rater_zip = models.TextField(max_length=10)

    @property
    def url(self):
        return reverse('rater_detail', args=[self.pk])

    def rating_count(self):
        return self.rating_set.count()

    def __repr__(self):
        return self.rater_job


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
        return self.movie_title


class Rating(models.Model):
    rater = models.ForeignKey(Rater, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField(default=0)
    time_stamp = models.IntegerField(default=0)

    def __repr__(self):
        return str(self.rating)
