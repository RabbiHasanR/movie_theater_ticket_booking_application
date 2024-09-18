from django.db.models import OuterRef, Exists
from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Movie, Seat, Booking

def index(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    
    return render(request, 'index.html', context)


def room_movies(request, room_id):
    room = get_object_or_404(Room.objects.prefetch_related('movies'), id=room_id)
    context = {
        'room': room,
        'movies': room.movies.all()
    }
    
    return render(request, 'room_movies.html', context)

def movie_seats(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    
    is_booked_subquery = Booking.objects.filter(movie=movie, seat_id=OuterRef('pk'))

    seats = Seat.objects.filter(room=movie.room).annotate(is_booked=Exists(is_booked_subquery))

    context = {
        'movie': movie,
        'seats': seats
    }
    return render(request, 'movie_seats.html', context)

def book_seat(request, movie_id, seat_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seat = get_object_or_404(Seat, id=seat_id)
    if not Booking.objects.filter(movie=movie, seat=seat).exists():
        Booking.objects.create(movie=movie, seat=seat)
    return redirect('movie_seats', movie_id=movie.id)
    



