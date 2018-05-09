""" Define URL patter for the Learning Logs app """
from django.conf.urls import url
from django.urls import path
from . import views

app_name = "Learning Logs"

urlpatterns = [
    # Homepage
    path('', views.index, name='index'),
    url(r'^$', views.index, name='index'),
]