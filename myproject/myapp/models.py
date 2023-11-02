from django.db import models

# Define your data model
class Target(models.Model):
    name = models.CharField(max_length=100)
    host = models.CharField(max_length=100)

    def __str__(self):
        return self.name