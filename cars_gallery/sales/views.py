from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Sale
from employees.models import Employee
from employees.serializer import EmpModelSerializer , EmpSerializer
from .serializers import SaleModelSerializer , TimeSerializer ,SaleSerializer2 , SaleSerializer
from cars.serializers import CarSearchSerializer , CarModelSerializer
from django.db.models import Count
from django.db.models import Max
from datetime import datetime, timezone
import datetime
from datetime import datetime as dt
@api_view(['GET'])
def maxSalesEmployee(request):
    x =[]
    emp= Employee.objects.all().count()
    for c in range(emp):
        data = Sale.objects.filter(employee = c).count()
        x.append(data)
    max = x[0]
    index = 0
    for i in range(1,len(x)):
        if x[i] > max:
            max = x[i] 
            index = i
    employ= Employee.objects.get(id=index)
    # serializer = EmpSerializer(data = employ)
    # if serializer.is_valid():
    return Response({'name' : employ.name} , status=status.HTTP_200_OK)

    #   return Response(serializer.data , status= status.HTTP_200_OK)
    # return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def SalesEmployee(request):
    w = SaleSerializer(data=request.data)
    if w.is_valid():
        serializer = w.data
        data = Employee.objects.filter(name = serializer['name'])
        m = SaleSerializer2(data , many = True)
        return Response(m.data, status= status.HTTP_200_OK)
    return Response(w.errors , status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def FourMostCarsSales(request):
    data = Sale.objects.values('car').annotate(sales=Count('car__id')).order_by('-sales')[:4]
    return Response(data, status= status.HTTP_200_OK)

@api_view(['GET'])
def FiveMostClientsSales(request):
    data = Sale.objects.values('client').annotate(sales=Count('client__id')).order_by('-sales')[:5]
    return Response(data, status= status.HTTP_200_OK)

@api_view(['GET'])
def BranchSales(request):
    data = Sale.objects.values('branch').annotate(sales=Count('branch__id')).order_by('-sales')[:]
    return Response(data, status= status.HTTP_200_OK)

@api_view(['GET'])
def MaxBranchSales(request):
    data = Sale.objects.values('branch').annotate(sales=Count('branch__id')).order_by('-sales')[:1]
    return Response(data, status= status.HTTP_200_OK)

@api_view(['GET'])
def TodaySales(request):
    timeSerializer = TimeSerializer(data = request.data)
    if timeSerializer.is_valid():
        timeData = timeSerializer.data
        t1= timeData['time1']
        sales = Sale.objects.filter(date=t1)
        serializer = SaleModelSerializer(sales , many = True)
        return Response(serializer.data , status= status.HTTP_200_OK)
    return Response(TimeSerializer.errors , status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def SalesInTime(request):
    timeSerializer = TimeSerializer(data = request.data)
    if timeSerializer.is_valid():
        timeData = timeSerializer.data
        t1= timeData['time1']
        t2= timeData['time2']
        sales = Sale.objects.filter(date__range=[t1, t2])
        serializer = SaleModelSerializer(sales , many = True)
        return Response(serializer.data , status= status.HTTP_200_OK)
    return Response(TimeSerializer.errors , status= status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def SalesInDaysAndHours(request):
#     timeSerializer = TimeSerializer(data = request.data)
#     if timeSerializer.is_valid():
#         timeData = timeSerializer.data
#         t1= timeData['time1']
#         input_date = t1
#         from_date = dt.strptime(input_date, '%Y-%m-%d').date()
#         from_date = datetime.datetime.combine(from_date, datetime.time.min)
#         to_date = datetime.datetime.combine(from_date, datetime.time.max)
#         sales = Sale.objects.filter(date = t1 , time__range = (from_date, to_date))
#         serializer = SaleModelSerializer(sales , many = True)
#         return Response(serializer.data , status= status.HTTP_200_OK)
#     return Response(TimeSerializer.errors , status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def SalesInDaysAndHours(request):
    timeSerializer = TimeSerializer(data = request.data)
    h = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
    # min = ["00","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59"]
    if timeSerializer.is_valid():
        timeData = timeSerializer.data
        t1= timeData['time1']
    for q in h:
        sales = Sale.objects.filter(date = t1 , time = q)
        serializer = SaleModelSerializer(sales , many = True)
        return Response(serializer.data , status= status.HTTP_200_OK)
    return Response(TimeSerializer.errors , status= status.HTTP_400_BAD_REQUEST)
