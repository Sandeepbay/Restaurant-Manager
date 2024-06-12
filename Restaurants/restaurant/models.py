from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=32 , blank=False)
    cuisine = models.CharField(max_length=10 , blank=False)
    rating = models.IntegerField(blank=False)
    reservation = models.BooleanField()

    def __str__(self):
        return f"{self.id}: {self.name}"

