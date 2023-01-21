from django.urls import path
from . import views

urlpatterns = [
    path('category/create/', views.createCategory ,name='createCategory'),
    path('<int:category_id>/category/', views.getByCategoryID ,name='getByCategoryID'),
    path('<str:category_name>/category/', views.getByCategoryName ,name='getByCategoryName'),
    path('<str:category_name>/count/', views.CountOfCar ,name='CountOfCar'),
    path('<int:id>/delete/', views.deleteCategory ,name='deleteCategory'),
    path('<int:id>/update/', views.updateCategory ,name='updateCategory'),
]