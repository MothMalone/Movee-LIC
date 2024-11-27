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

