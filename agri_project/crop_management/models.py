from django.db import models

class Crop(models.Model):
    name = models.CharField(max_length=100)
    season = models.CharField(max_length=50)
    cultivation_method = models.TextField()
    advice = models.TextField()

    def __str__(self):
        return self.name
