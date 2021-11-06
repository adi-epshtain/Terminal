from django.db import models


class Flight(models.Model):

    # "id" serial NOT NULL PRIMARY KEY
    arrival = models.CharField(max_length=8, null=False, blank=False, verbose_name='arrival time')
    departure = models.CharField(max_length=8, null=False, blank=False, verbose_name='departure time')
