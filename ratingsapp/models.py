from django.db import models
from django.db.models import Avg
from django.urls import reverse
from django.contrib.auth.models import User


class Rater(models.Model):
    rater_age = models.IntegerField(default=0)
    rater_gender = models.CharField(max_length=1)
    rater_job = models.CharField(max_length=20)
    rater_zip = models.CharField(max_length=10)
    user = models.OneToOneField(User, null=True)


    @property
    def url(self):
        return reverse('rater_detail', args=[self.pk])

    def rating_count(self):
        return self.rating_set.count()

    def __str__(self):
        return str(self.id)


class Movie(models.Model):
    movie_title = models.CharField(max_length=100)

    @property
    def url(self):
        return reverse('movie_detail', args=[self.pk])

    def avg_rating(self):
        r_set = self.rating_set.all()
        if len(r_set) == 0:
            return 0
        else:
            average = r_set.aggregate(Avg('rating'))
            return round(average["rating__avg"], 2)

    def __str__(self):
        return self.movie_title


class Rating(models.Model):
    rater = models.ForeignKey(Rater, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rating = models.FloatField(default=0)
    time_stamp = models.IntegerField(default=0)

    def __str__(self):
        return str(self.rating) + str(self.movie)


class RatingForm(models.Model):
    pass

class UserForm(models.Model):
    pass


# class UserProfile(models.Model):
#     # This field is required.
#     rater_age = models.IntegerField(default=0)
#     rater_gender = models.CharField(max_length=1)
#     rater_job = models.CharField(max_length=20)
#     rater_zip = models.TextField(max_length=10)
#     user = models.OneToOneField(User)
#
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserProfile.objects.create(user=instance)
#
#     post.save.connect(create_user_profile, sender=User)

def fill_users():
    for r in Rater.objects.all():
        rid = "R"+str(r.id)
        r.user = User.objects.create_user(
            username=rid, email="a@example.org", password="pass"
        )
        r.user.set_password("pass")
        r.user.save()
        r.save()
