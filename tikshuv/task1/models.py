from django.db import models

# Create your models here.


# Colors Model
class Color(models.Model):
    name = models.CharField(max_length=15)

# Department Model


class Department(models.Model):
    name = models.CharField(max_length=20)

# Employee Model


class Employee(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    is_senior = models.BooleanField()
    favorite_color = models.ForeignKey(Color, on_delete=models.CASCADE)
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
