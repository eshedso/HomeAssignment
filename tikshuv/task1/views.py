from django.shortcuts import render
from django.http import HttpResponse
from . import models
# Create your views here.


def indexView(request):
    queryset = models.Department.objects.all().order_by('id')
    context = {}
    context['departments'] = {}
    for i in queryset:
        context['departments'][i.id] = i.name
    return render(request, 'html/index.html', context)


def departmentView(request, department_name):
    try:
        queryset = models.Department.objects.get(name=department_name)
        return HttpResponse(department_name)
    except:
        return HttpResponse("404 NOT FOUND")
