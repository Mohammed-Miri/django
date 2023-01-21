from django.urls import path
from . import views

urlpatterns = [
    path('create-user/', views.createUser ,name='createUser'),
    path('<str:name>/delete/', views.deleteUserByName ,name='deleteUserByName'),
    path('<int:id>/update/', views.updateUser ,name='updateUser'),
]