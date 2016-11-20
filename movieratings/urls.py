from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
import ratingsapp


urlpatterns = [
    url(r'^ratingsapp/', include('ratingsapp.urls')),
    url(r'^logout/$', auth_views.logout, {'next_page': '/login/'}, name='logout'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^create_user/$', ratingsapp.views.create_user, name='create_user'),
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^ratingsapp/profile/$', ratingsapp.views.profile,
        name='user_profile'),
]
