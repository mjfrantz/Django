from django.db import models
from movies.models import Genre, Movie, Series
from tastypie.resources import ModelResource, fields, ALL
from tastypie.authorization import Authorization

class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movies'
        ordering = ["release_year", "title", "price"]
        filtering = {
            'release_year':ALL,
            'price': ALL,
            'title': ALL,
            'in_stock': ALL,
            'duration_mins': ALL
        }

class GenreResource(ModelResource):
    class Meta: 
        queryset = Genre.objects.all()
        resource_name = 'genres'
        allowed_method = ['get', 'post', 'put', 'patch', 'delete'] 
        authorization = Authorization()

# class SeriesResource(ModelResource):
#     class Meta:
#         queryset = Series.objects.all()
#         resource_name = 'series'

""" 
var g = { name: 'test'}


"""

""" 
/api/movies/?order_by=price
/api/movies/?order_by=-price

/api/movies

/api/movies/?price=4.99

/api/movies/?release_year__gt=2015

/api/movies/?title__contains=Night

/api/movies/?duration_mins__gt=100


"""