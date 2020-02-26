from django.db import models

# Create your models here.

class Notes(models.Model):
    item = models.CharField(max_length=80)
    description = models.TextField(max_length=300)

    def __str__(self):
        return f"Note item: {self.item} description: {self.description}"