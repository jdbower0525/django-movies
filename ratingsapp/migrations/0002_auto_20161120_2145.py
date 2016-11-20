# Generated by Django 1.10.3 on 2016-11-16 21:32
from __future__ import unicode_literals
from django.db import migrations
import csv

def add_raters(apps, schema_editor):
    with open('u.user.csv', 'r') as f:
        # fieldnames = ['rater_age', 'rater_gender', 'rater_job', 'rater_zip']
        r = csv.reader(f, delimiter='|')
        Rater = apps.get_model('ratingsapp', 'Rater')
        for line in r:
            b = Rater(*line)
            b.save()


def add_movies(apps, schema_editor):
    with open('u.item.csv', encoding='latin_1') as f:
        r = csv.reader(f, delimiter='|')
        Movie = apps.get_model('ratingsapp', 'Movie')
        for line in r:
            b = Movie(line[0], line[1][:-7])
            b.save()


def add_ratings(apps, schema_editor):
    with open('u.data.csv', 'r') as f:
        # fieldnames = ['rater_age', 'rater_gender', 'rater_job', 'rater_zip']
        r = csv.DictReader(f, fieldnames=['rater_id', 'movie_id',
                           'rating', 'time_stamp'], delimiter='\t')
        Rating = apps.get_model('ratingsapp', 'Rating')
        for line in r:
            b = Rating(**line)
            b.save()



class Migration(migrations.Migration):

    dependencies = [
        ('ratingsapp', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_raters),
        migrations.RunPython(add_movies),
        migrations.RunPython(add_ratings),
    ]