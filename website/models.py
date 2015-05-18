from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=100, unique=True)
    rating = models.FloatField()
    type = models.PositiveSmallIntegerField(default=1)
    cover = models.ImageField()
