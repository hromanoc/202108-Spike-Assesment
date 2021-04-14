from django.db import models

# Create your models here.

class Distance(models.Model):
    origin = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    distance = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"La distancia desde {self.origin} hacia {self.destination} es de {self.distance} kms"