from django.db import models

# Create your models here.
class student(models.Model):
    first_name=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    total_marks=models.IntegerField(auto_created=True)
    date_of_birth=models.DateField(auto_created=True)
