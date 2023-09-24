from django.db import models

# Model representing a Railway
class Railway(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

# Model representing a Siding (coal storage area)
class CoalStock(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    capacity = models.IntegerField()  # Capacity in tons
    available_space = models.IntegerField()  # Available space in tons
    last_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

