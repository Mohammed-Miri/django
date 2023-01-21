from django.db.models import Q
from rest_framework.decorators import api_view, parser_classes ,renderer_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import JSONParser , FormParser , MultiPartParser
from rest_framework.renderers import JSONRenderer , BrowsableAPIRenderer
from .serializers import (
    CarModelSerializer,
    CarSerializer,
    CarSearchSerializer,
    CarSearchSerializer2,
    CarSerializer2
    )

from .models import Car


@api_view(['POST'])
def createCar(request):
    serializer = CarModelSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status= status.HTTP_201_CREATED)
    return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def createCar2(request):
    serializer = CarSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status= status.HTTP_201_CREATED)
    return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)

@api_view(['delete'])
def deleteCar(request , id):
    try:
        car= Car.objects.get(pk=id)
        try:
            car.delete()
            return Response ({},status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({} , status=status.HTTP_400_BAD_REQUEST)
    except Car.DoesNotExist:
        return Response ({},status=status.HTTP_404_NOT_FOUND)

@api_view(['delete'])
def deleteCarByName(request , name):
    try:
        Car= Car.objects.filter(name = name)
        try:
            Car.delete()
            return Response ({},status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({} , status=status.HTTP_400_BAD_REQUEST)
    except Car.DoesNotExist:
        return Response ({},status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def updateCar(request , id):
    try:
        car = Car.objects.get(pk= id)
        serializer = CarModelSerializer(data= request.data , instance= car)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_202_ACCEPTED )
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
    except:
        return Response({} , status= status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def updateCar2(request , id):
    try:
        car = Car.objects.get(pk= id)
        serializer = CarSerializer(data= request.data , instance= car)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_202_ACCEPTED )
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
    except:
        return Response({} , status= status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def searchByCarId(request , id):
    try:
        car = Car.objects.get(pk=id)
        serializer = CarSerializer(car)
        # return Response({'name' : car.name} , status=status.HTTP_200_OK)
        return Response(serializer.data , status= status.HTTP_200_OK)
    except Car.DoesNotExist:
        return Response({} , status= status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def searchByCarName(request):
    searchSerializer = CarSearchSerializer(data = request.data)
    if searchSerializer.is_valid():
        searchData = searchSerializer.data
        car= Car.objects.filter(name = searchData['name'])
        carSerializer = CarModelSerializer(car , many = True)
        return Response(carSerializer.data , status= status.HTTP_200_OK)
    return Response(searchSerializer.errors , status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def searchByNameAndCategoryAndPriceRange(request):
    searchSerializer = CarSearchSerializer2(data = request.data)
    if searchSerializer.is_valid():
        searchData = searchSerializer.data
        p1= searchData['price1']
        p2= searchData['price2']
        car= Car.objects.filter(Q(Q(name__icontains = searchData['name'])|Q(arabic_name__contains = searchData['name'])))
        car = car.filter(price__range=[p1, p2] , category = searchData['category'])
        carSerializer = CarSerializer2(car , many = True)
        return Response(carSerializer.data , status= status.HTTP_200_OK)
    return Response(searchSerializer.errors , status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def searchByNameAndCategoryAndPrice(request):
    searchSerializer = CarSearchSerializer2(data = request.data)
    if searchSerializer.is_valid():
        searchData = searchSerializer.data
        p1= searchData['price1']
        p2= searchData['price2']
        car= Car.objects.filter(name__icontains = searchData['name'] , price__lte = p2 , price__gte = p1 , category = searchData['category'])
        carSerializer = CarModelSerializer(car , many = True)
        return Response(carSerializer.data , status= status.HTTP_200_OK)
    return Response(searchSerializer.errors , status= status.HTTP_400_BAD_REQUEST)