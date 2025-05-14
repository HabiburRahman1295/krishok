from django.db import models

class Krishok(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique=True)
    nid = models.CharField(max_length=20, unique=True)
    birth_certificate = models.FileField(upload_to='birth_certificates/')

    def __str__(self):
        return self.name
