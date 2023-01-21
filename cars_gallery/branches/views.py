from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import BranchModelSerializer, SearchSerializer ,BranchSerializer2 ,BranchSerializer , CarBranchSerializer , EmployeeBranchSerializer
from cars.serializers import CarModelSerializer ,CarSearchSerializer
from employees.serializer import EmpModelSerializer
from sales.serializers import SaleModelSerializer
from .models import Branch
from cars.models import Car
from employees.models import Employee
from sales.models import Sale

@api_view(['GET'])
def getByBranchId(request , id):
    try:
        branch = Branch.objects.get(pk=id)
        serializer = BranchModelSerializer(branch)
        return Response(serializer.data , status= status.HTTP_200_OK)
    except Branch.DoesNotExist:
        return Response({} , status= status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def getCarsByBranchId(request , id):
    cars = Car.objects.filter(branch = id)
    serializer = CarModelSerializer(cars , many = True)
    return Response(serializer.data , status= status.HTTP_200_OK)        


@api_view(['GET'])
def getCarsAndEmployees(request):
    w = SearchSerializer(data=request.data)
    if w.is_valid():
        serializer = w.data
        data = Branch.objects.filter(name = serializer['name'])
        m = BranchSerializer2(data , many = True)
        return Response(m.data, status= status.HTTP_200_OK)
    return Response(w.errors , status= status.HTTP_400_BAD_REQUEST)
