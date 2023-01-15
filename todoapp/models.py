from django.db import models
from django.contrib.auth.models import User


class TodoDatabase(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField()
    deadline = models.DateField()

    def __str__(self):
        return self.title



# Create your models here.
