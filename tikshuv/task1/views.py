from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.


def index(request):
    queryset = models.Department.objects.all().order_by('id')
    context = {}
    context['departments'] = {}
    for i in queryset:
        context['departments'][i.id] = i.name
    return render(request, 'html/index.html', context)
