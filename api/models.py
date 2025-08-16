from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)