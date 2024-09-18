from django.contrib import admin
from .models import Room, Seat, Movie, Booking


admin.site.register(Room)
admin.site.register(Seat)
admin.site.register(Movie)
admin.site.register(Booking)
