from django.db import models

class Product(models.Model):
    krishok_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price_per_unit = models.FloatField()
    seller_type = models.CharField(max_length=20, choices=[('wholesale', 'পাইকারী'), ('retail', 'খুচরা')])

    def __str__(self):
        return f"{self.name} ({self.krishok_name})"
