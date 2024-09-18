from django.shortcuts import render, get_object_or_404
from .models import Room, Movie

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



