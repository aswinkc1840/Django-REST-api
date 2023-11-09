from django.db import models

# Create your models here.
from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Theater(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Ticket(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    time = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    seats_available = models.IntegerField()

    def __str__(self):
        return f"{self.movie} - {self.theater} - {self.time}"
