from django.db import models
from django.utils import timezone
  
class Dareupload(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    level = models.CharField(max_length=20)
    dare = models.TextField()
    duration = models.CharField(max_length=50, blank=True)
    safety = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
