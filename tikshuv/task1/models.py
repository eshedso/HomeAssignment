from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.


# Colors Model
class Color(models.Model):
    name = models.CharField(max_length=15, null=False, unique=True)

# Department Model


class Department(models.Model):
    name = models.CharField(max_length=20, null=False, unique=True)

# Employee Model


def get_default_color():
    try:
        return Color.objects.get(name='White').id
    except:
        return None


def get_default_department():
    try:
        return Department.objects.get(id=1).id
    except:
        return None


class Employee(models.Model):
    name = models.CharField(max_length=30, null=False)
    age = models.IntegerField(null=False)
    is_senior = models.BooleanField(default=False, null=False)
    favorite_color = models.ForeignKey(
        Color, on_delete=models.CASCADE, default=get_default_color)
    Department = models.ForeignKey(
        Department, on_delete=models.CASCADE, default=get_default_department)
    # age validation

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 18 or age > 120:
            raise ValidationError(
                "Age must be a number in the range of 18~120")
        return age
