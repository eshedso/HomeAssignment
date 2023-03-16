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
   # try:
    departmentset = models.Department.objects.get(name=department_name)
    employeeset = list(models.Employee.objects.filter(
        Department_id=departmentset.id))
    colorset = models.Color.objects.all()
    context = {}
    context['employees'] = [employeeset[counter: counter+5]
                            for counter in range(0, len(employeeset), 5)]
    context['colors'] = list(colorset)
    return render(request, 'html/employees.html', context)
    # except:
 #   pass
