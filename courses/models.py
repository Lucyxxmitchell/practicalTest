from django.db import models

# Create your models here.
class Courses(models.Model):
    title = models.CharField(max_length=128, unique=True)
    startDate = models.DateField()
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title

