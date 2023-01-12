from django.db import models

class TodoDatabase(models.Model):
    title = models.CharField(max_length=300)
    description = models.TextField()
    deadline = models.DateField()

    def __str__(self):
        return self.title



# Create your models here.
