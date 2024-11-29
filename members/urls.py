from django.urls import path
from . import views

urlpatterns  = [
    path('members/', views.members, name = 'members'),
    path('', views.home, name = "home"),
    path('members/detail/<int:id>', views.detail, name='details'),
    path('player/<int:id>', views.player, name = "player"),
    path('movies/', views.movies, name = 'movies'),
    path('tvseries', views.tvseries, name = 'tvseries'),
    path('tvseries/<int:id>', views.tvseries_detail, name = 'tvseries_detail'),
    
]