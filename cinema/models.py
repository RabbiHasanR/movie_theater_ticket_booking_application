from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField() 
    columns = models.IntegerField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='posters/')
    show_time = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return f"{self.title} at {self.show_time}"

class Seat(models.Model):
    row = models.IntegerField()
    column = models.IntegerField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='seats')

    def __str__(self):
        return f"Seat {self.row}-{self.column} in {self.room.name}"

class Booking(models.Model):
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE, related_name='bookings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='bookings')
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"Booking for {self.movie.title} - Seat {self.seat.row}-{self.seat.column}"
