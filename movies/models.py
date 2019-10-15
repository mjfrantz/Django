from django.db import models

# Create your models here.

"""
    field: 
    Char (string)
    Int
    Float
    Boolean
"""

class Genre(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=250)
    release_year = models.IntegerField()
    in_stock = models.IntegerField()
    price = models.FloatField()
    duration_mins = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


