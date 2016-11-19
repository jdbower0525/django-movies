from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
#from . import views
#import ratingsapp

urlpatterns = [
    url(r'^ratingsapp/', include('ratingsapp.urls')),
    url(r'^login/$', auth_views.login, name='login'),
    # url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^accounts/profile/$', TemplateView.as_view(
                    template_name='profile.html'), name='user_profile')
]
