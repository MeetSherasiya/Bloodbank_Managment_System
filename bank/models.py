from django.db import models

# Create your models here.
class Blood(models.Model):
    name = models.CharField(max_length=10)
    unit = models.IntegerField(default=0)

    def __str__(self):
        return self.name