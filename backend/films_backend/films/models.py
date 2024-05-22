from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime
from taggit.managers import TaggableManager


class Film(models.Model):
    name = models.CharField(max_length=128)
    release_year = models.IntegerField(validators=[
        MinValueValidator(1900),
        MaxValueValidator(datetime.now().year)
    ],
        default=datetime.now().year
    )
    description = models.TextField(max_length=356)
    director = models.CharField(max_length=128)
    image = models.ImageField(upload_to='images/')
    tags = TaggableManager()

    def __str__(self):
        return self.name
