from django.urls import path, re_path

from . import views

urlpatterns = [
    path(r'', views.indexView, name='indexView'),
    re_path(r'^(?P<department_name>[a-zA-Z]+)/$',
            views.departmentView, name="DepartmentView")
]
