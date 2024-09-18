from django.shortcuts import render
from .models import Room

def index(request):
    rooms = Room.objects.all()
    context = {
        'rooms': rooms
    }
    
    return render(request, 'index.html', context)
