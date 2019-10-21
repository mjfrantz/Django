from django.db import models
from movies.models import Genre, Movie, Series
from tastypie.resources import ModelResource, fields, ALL

class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        filtering = {
            'release_year':ALL,
            'price': ALL,
            'title': ALL,
            'in_stock': ALL
        },
        ordering = ["release_year", "title", "price"]

class GenreResource(ModelResource):
    class Meta: 
        queryset = Genre.objects.all()
        resource_name = 'genres'

# class SeriesResource(ModelResource):
#     class Meta:
#         queryset = Series.objects.all()
#         resource_name = 'series'