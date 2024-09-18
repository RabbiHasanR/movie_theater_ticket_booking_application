import os
from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import Movie

@receiver(post_delete, sender=Movie)
def delete_movie_poster(sender, instance, **kwargs):
    if instance.poster:
        poster_path = instance.poster.path
        if os.path.isfile(poster_path):
            os.remove(poster_path)
