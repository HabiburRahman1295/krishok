from django.db import models

class Advisory(models.Model):
    farmer_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    question = models.TextField()
    answer = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.farmer_name} - {self.question[:30]}..."
