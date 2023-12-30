from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    completed = models.BooleanField(default=False, blank=True)
    create_ad = models.DateTimeField(auto_now=True)
