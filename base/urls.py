from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^movie-list/$', views.movieAPI),
    re_path(r'^movie-vote/$', views.movieVoteAPI),
    re_path(r'^actor-list/$', views.actorAPI)
]
