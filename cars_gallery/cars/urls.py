from django.urls import path
from . import views

urlpatterns = [
    path('search-by-car-id/<int:id>/',views.searchByCarId,name='searchByCarId'),
    path('search-by-car-name/',views.searchByCarName , name ='searchByCarName'),
    path('search-by/',views.searchByNameAndCategoryAndPrice , name ='searchByNameAndCategoryAndPrice'),
    path('search-by-range/',views.searchByNameAndCategoryAndPriceRange , name ='searchByNameAndCategoryAndPriceRange'),
    path('create-car/', views.createCar ,name='createCar'),
    path('create-car2/', views.createCar2 ,name='createCar2'),
    path('<int:id>/delete/', views.deleteCar ,name='deleteCar'),
    path('<int:id>/update/', views.updateCar ,name='updateCar'),
    path('<int:id>/update2/', views.updateCar2 ,name='updateCar2'),
]