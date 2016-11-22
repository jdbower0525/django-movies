from django import forms
from django.contrib.auth.models import User
from ratingsapp.models import Rater, Rating


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class RaterForm(forms.ModelForm):
    class Meta:
        model = Rater
        fields = ['rater_age', 'rater_gender', 'rater_job', 'rater_zip']


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        #fields = ['rater', 'movie', 'rating', 'time_stamp']
        fields = '__all__'


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')
