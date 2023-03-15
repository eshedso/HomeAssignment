from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


# Colors Model
class Color(models.Model):
    name = models.CharField(max_length=15, null=False)

# Department Model


class Department(models.Model):
    name = models.CharField(max_length=20, null=False)

# Employee Model


class Employee(models.Model):
    name = models.CharField(max_length=30, null=False)
    age = models.IntegerField(null=False)
    is_senior = models.BooleanField(default=False, null=False)
    favorite_color = models.ForeignKey(
        Color, on_delete=models.CASCADE, null=False)
    Department = models.ForeignKey(
        Department, on_delete=models.CASCADE, null=False)
    # age validation

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18 or age > 120:
            raise ValidationError(
                "Age must be a number in the range of 18~120")
        return age
