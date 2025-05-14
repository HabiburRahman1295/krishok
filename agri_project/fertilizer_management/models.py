from django.db import models

class Fertilizer(models.Model):
    name = models.CharField(max_length=100)
    crop_type = models.CharField(max_length=100)
    usage_time = models.CharField(max_length=100)
    dosage = models.CharField(max_length=100)
    recommendation = models.TextField()

    def __str__(self):
        return f"{self.name} for {self.crop_type}"
