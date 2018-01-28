from django.db import models

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    image = models.CharField(max_length=150)
    source = models.CharField(max_length=150, blank=True, default='')

class Painting(models.Model):
    name = models.CharField(max_length=150)
    artist = models.ForeignKey(Artist, related_name='paintings', on_delete=models.CASCADE)
    description = models.TextField()
    retail_price = models.FloatField()
    price = models.FloatField()
    image = models.CharField(max_length=150)
    source = models.CharField(max_length=150, blank=True, default='')