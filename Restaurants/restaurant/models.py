from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=32 , blank=False)
    cuisine = models.CharField(max_length=10 , blank=False)
    rating = models.IntegerField(blank=False)
    reservation = models.BooleanField()

    def __str__(self):
        return f"{self.id}: {self.name}"
    
class People(models.Model):
    name = models.CharField(max_length=32 , blank=False)
    order = models.CharField(max_length=32 , blank=False)
    review = models.CharField(max_length=50)
    conneection = models.ManyToManyField(Restaurant , blank=False , related_name="people")

    def __str__(self):
        return f"{self.id} : {self.name} - {self.order}"



