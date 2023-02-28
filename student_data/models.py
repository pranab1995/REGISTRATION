from django.db import models

# Create your models here.

class Student(models.Model):
    title = models.CharField(max_length=200)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    country = models.CharField(max_length=200)
    message = models.TextField(max_length=200)
    password = models.CharField(max_length=200)
    

    def __str__(self):
        return self.first_name + self.last_name