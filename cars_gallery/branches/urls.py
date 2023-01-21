from django.urls import path
from . import views

urlpatterns = [
    path('get-by-branch-id/<int:id>/',views.getByBranchId,name='getByBranchId'),
    path('get-cars-by-branch-id/<int:id>/',views.getCarsByBranchId,name='getCarsByBranchId'),
    path('get-cars-and-employees/',views.getCarsAndEmployees,name='getCarsAndEmployees'),
]