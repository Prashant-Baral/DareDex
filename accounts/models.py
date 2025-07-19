from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Student(User):
    GENDER_CHOICES = (
        ("Male","Male"),
        ("Female","Female"),
        ("Other","Other")
    )
    name = models.CharField(max_length=13)
    gender = models.CharField(max_length = 10,choices= GENDER_CHOICES)
    profile = models.ImageField(upload_to = 'user_profile')

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

