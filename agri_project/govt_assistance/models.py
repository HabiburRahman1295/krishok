from django.db import models

class AssistanceApplication(models.Model):
    ASSISTANCE_CHOICES = [
        ('loan', 'ঋণ সহায়তা'),
        ('subsidy', 'সাবসিডি'),
        ('equipment', 'কৃষিযন্ত্র সহায়তা'),
        ('training', 'প্রশিক্ষণ/শিক্ষা'),
    ]

    krishok_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    assistance_type = models.CharField(max_length=20, choices=ASSISTANCE_CHOICES)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.krishok_name} - {self.assistance_type}"
