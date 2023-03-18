
from django import forms
from django.forms.models import ModelForm
from django.http.response import HttpResponse
from . import models


class employeeForm(forms.Form):
    id = forms.IntegerField(required=True)
    color = forms.CharField(max_length=15, required=False)
    is_senior = forms.BooleanField(required=False)

    def clean_id(self):
        _id = self.cleaned_data.get('id')
        try:
            employee = models.Employee.objects.get(id=_id)
        except models.Employee.DoesNotExist:
            raise forms.ValidationError("Employee does not exist")
        return _id

    def clean_color(self):
        _color = self.cleaned_data.get('color')
        try:
            if (_color):
                color = models.Color.objects.get(name=_color)
            else:
                color = None
        except models.Color.DoesNotExist:
            raise forms.ValidationError("Color Does not Exist")
        return color

    def clean_is_senior(self):
        _is_senior = self.cleaned_data.get('is_senior')
        print('here')
        try:
            if _is_senior:
                return _is_senior
            return False
        except:
            raise forms.ValidationError("Seniority error")
