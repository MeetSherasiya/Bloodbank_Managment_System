from django.db import models
from django.conf import settings

Blood = [
    ("O+", "O+"),
    ("O-", "O-"),
    ("A+", "A+"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
]

Progress = [
    ("Pending", "Pending"),
    ("Approved", "Approved"),
    ("Reject", "Reject"),
]

# Create your models here.
class BloodDonate(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=200)
    patient_age = models.IntegerField(default=0)
    disease = models.TextField()
    bloodgroup = models.CharField(max_length=5, choices=Blood)
    unit = models.IntegerField(default=0)
    progress = models.CharField(max_length=30, choices=Progress, default="Pending")
    Donate_Date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name
