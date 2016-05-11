from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Top_spots (models.Model):
    image = models.ImageField(upload_to='photos', verbose_name='My Photo')
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)