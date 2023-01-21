from django.urls import path
from . import views

urlpatterns =[
        path('max-sales/',views.maxSalesEmployee,name='maxSalesEmployee'),
        path('sales-employee/',views.SalesEmployee,name='SalesEmployee'),
        path('four-most-cars-sales/',views.FourMostCarsSales,name='FourMostCarsSales'),
        path('five-most-clients-sales/',views.FiveMostClientsSales,name='FiveMostClientsSales'),
        path('branch-sales/',views.BranchSales,name='BranchSales'),
        path('max-branch-sales/',views.MaxBranchSales,name='MaxBranchSales'),
        path('today-sales/',views.TodaySales,name='TodaySales'),
        path('sales-in-time/',views.SalesInTime,name='SalesInTime'),
        path('sales-in-days-and-hours/',views.SalesInDaysAndHours,name='SalesInDaysAndHours'),
]