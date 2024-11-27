from django.db import models
import ffmpeg
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class Member(models.Model):
    id = models.IntegerField(primary_key= True)
    avatar = models.URLField(blank= True)
    username = models.CharField(max_length=255, unique= True, null= False)
    password = models.CharField(max_length=255, null = False)
    firstname = models.CharField(max_length=255, null = True)
    lastname = models.CharField(max_length=255, null = True)
    phone = models.CharField(max_length= 20, null = True)
    email = models.CharField(max_length= 255, null= True)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
class Genre(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    movies = models.ManyToManyField('Movie', related_name="genre_list", blank = True)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=255, blank=False, unique=True)
    dob = models.DateField(blank=True)
    image = models.URLField(blank=True)
    films = models.ManyToManyField('Movie', related_name="actor_list", blank = True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=255, null=False, unique=True)
    description = models.TextField(null=True, unique=False)
    source = models.CharField(max_length=255, null=True)
    source1 = models.CharField(blank=True, max_length=255)
    image_src = models.CharField(max_length=255, null=True)
    subtitle = models.TextField(blank=True)
    genres = models.ManyToManyField(Genre, related_name="movie_list", blank=True)

    def __str__(self):
        return self.title

class TVSeries(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    release_date = models.DateField(null=True, blank=True)
    genre = models.CharField(max_length=100, blank=True)
    seasons = models.PositiveIntegerField(default=1)
    episodes = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    thumbnail = models.TextField(blank=True)
    def __str__(self):
        return self.title
