from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('room/<int:room_id>/', views.room_movies, name='room_movies'),
    path('movie/<int:movie_id>/seats/', views.movie_seats, name='movie_seats'),
    path('movie/<int:movie_id>/seat/<int:seat_id>/book/', views.book_seat, name='book_seat'),
]