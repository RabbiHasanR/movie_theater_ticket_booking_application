import itertools
from django.db import models
from datetime import timedelta
from django.core.exceptions import ValidationError

class Room(models.Model):
    name = models.CharField(max_length=100)
    rows = models.IntegerField() 
    columns = models.IntegerField()

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.update_seats()

    def update_seats(self):
        existing_seats = Seat.objects.filter(room=self)

        existing_seat_positions = set((seat.row, seat.column) for seat in existing_seats)

        all_possible_seat_positions = set(itertools.product(range(1, self.rows + 1), range(1, self.columns + 1)))

        seats_to_create = all_possible_seat_positions - existing_seat_positions
        
        new_seats = [Seat(room=self, row=row, column=column) for row, column in seats_to_create]

        Seat.objects.bulk_create(new_seats)

        seats_to_delete = existing_seats.filter(row__gt=self.rows) | existing_seats.filter(column__gt=self.columns)

        seats_to_delete.delete()


class Movie(models.Model):
    title = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='posters/')
    show_time = models.DateTimeField()
    movie_length = models.IntegerField(help_text="Movie length in minutes")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='movies')

    def __str__(self):
        return f"{self.title} at {self.show_time}"

    def clean(self):
        new_movie_end_time = self.show_time + timedelta(minutes=self.movie_length + 30)

        overlapping_movies = Movie.objects.filter(
            room=self.room
        ).exclude(id=self.id)

        for movie in overlapping_movies:
            existing_movie_end_time = movie.show_time + timedelta(minutes=movie.movie_length + 30)

            if self.show_time < existing_movie_end_time and new_movie_end_time > movie.show_time:
                raise ValidationError(
                    f"Movie '{movie.title}' is already scheduled in {self.room.name} "
                    f"from {movie.show_time} to {existing_movie_end_time}. Please choose a different time."
                )

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

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
    
    
    class Meta:
        unique_together = ('movie', 'seat')

    def clean(self):
        if self.seat.room != self.movie.room:
            raise ValidationError("The selected seat does not belong to the room where the movie is being shown.")
