from django.conf.urls import url, include

from . import views
urlpatterns = [
  url(r'^$', views.emailView, name='emailView'),
  url(r'^success/$', views.successView, name='successView'),
]