from django.contrib import admin
from .models import Rater
from .models import Movie
from .models import Rating

# Register your models here.
admin.site.register(Rater)
admin.site.register(Movie)
admin.site.register(Rating)

# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-16 19:24
# from __future__ import unicode_literals
#
# from django.db import migrations
# import csv
#
# # 921|20|F|student|98801
#
# def add_raters(apps, schema_editor):
#     with open('u.user.csv', 'r') as f:
#         # fieldnames = ['rater_age', 'rater_gender', 'rater_job', 'rater_zip']
#         r = csv.reader(f, delimiter='|')
#         Rater = apps.get_model('ratingsapp', 'Rater')
#         for line in r:
#             print(line)
#             b = Rater(*line)
#             b.save()
#
#
# class Migration(migrations.Migration):
#
#     dependencies = [
#         ('ratingsapp', '0001_initial'),
#     ]
#
#     operations = [
#         migrations.RunPython(add_raters),
#     ]





# def add_movies(apps, schema_editor):
#     with open('u.item.csv', 'r') as f:
#         # fieldnames = ['rater_age', 'rater_gender', 'rater_job', 'rater_zip']
#         r = csv.reader(f, delimiter='|')
#         Movie = apps.get_model('ratingsapp', 'Movie')
#         for line in r:
#             print(line)
#             b = Movie(*line)
#             b.save()
#
#
#
# class Migration(migrations.Migration):
#
#     dependencies = [
#         ('ratingsapp', '0002_auto_20161116_2014'),
#     ]
#
#     operations = [
#         migrations.RunPython(add_movies),
#     ]
