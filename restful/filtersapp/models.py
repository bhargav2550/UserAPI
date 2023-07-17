from django.db import models

# Create your models here.

class users(models.Model):
    CHOICES = [("Male","Male"),("Female","Female"),("Don't want to say","None")]
    first_name = models.CharField(max_length= 40)
    last_name  = models.CharField(max_length= 40)
    age        = models.IntegerField()
    gender     = models.CharField(max_length=20)
    email      = models.EmailField()
    phone      = models.CharField(max_length=25)
    Birth_date = models.DateField()