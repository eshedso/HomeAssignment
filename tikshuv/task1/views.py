from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from . import forms
# Create your views here.


def indexView(request):
    queryset = models.Department.objects.all().order_by('id')
    context = {}
    context['departments'] = {}
    for i in queryset:
        context['departments'][i.id] = i.name
    return render(request, 'html/index.html', context)


def departmentView(request, department_name):
    context = {}
    if (request.method == 'GET'):
        try:
            departmentset = models.Department.objects.get(name=department_name)
            employeeset = list(models.Employee.objects.filter(
                Department_id=departmentset.id).order_by('id'))
            colorset = models.Color.objects.all().order_by('id')
            context['employees'] = [employeeset[counter: counter+5]
                                    for counter in range(0, len(employeeset), 5)]
            context['colors'] = list(colorset)
            context['department'] = department_name
            return render(request, 'html/employees.html', context)
        except models.Department.DoesNotExist:
            context['error'] = "Department not found"
        except:
            context['error'] = "General Error please advise"
        return render(request, 'html/error.html', context, status=404)
    elif (request.method == 'POST'):
        try:
            _form = forms.employeeForm(request.POST)
            if _form.is_valid():
                employee = models.Employee.objects.get(
                    id=_form.cleaned_data.get('id'))
                employee.favorite_color = _form.cleaned_data.get('color')
                employee.is_senior = _form.cleaned_data.get('is_senior')
                employee.save()
                return redirect('/task1/{0}'.format(department_name))
            else:
                context['error'] = "the form submitted is invalid"

        except (models.Employee.DoesNotExist, models.Color.DoesNotExist):
            context['error'] = "Employee/Color does not exist"
        except:
            context['error'] = "General Error please advise"
        return render(request, 'html/error.html', context, status=404)
