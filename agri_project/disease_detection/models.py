from django.db import models

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='crop_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
