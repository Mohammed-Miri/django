from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count


from .serializers import CategoryModelSerializer , CategorySerializer  , CountCategory
from cars.serializers import CarModelSerializer
from .models import Category
from cars.models import Car

@api_view(['POST'])
def createCategory(request):
    serializer = CategoryModelSerializer(data= request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data , status= status.HTTP_201_CREATED)
    return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getByCategoryID(request , category_id):
    data = Car.objects.filter(category = category_id)
    serializer = CarModelSerializer(data, many = True)
    return Response(serializer.data , status= status.HTTP_200_OK)

@api_view(['GET'])
def getByCategoryName(request , category_name):
    data = Car.objects.filter(category__name = category_name)
    serializer = CarModelSerializer(data , many = True)
    return Response(serializer.data , status= status.HTTP_200_OK)

@api_view(['GET'])
def CountOfCar(request , category_name):
    data = Car.objects.filter(category__name = category_name).count()
    result= {
        'count': data
    }
    return Response(result, status= status.HTTP_200_OK)

@api_view(['delete'])
def deleteCategory(request , id):
    try:
        category= Category.objects.get(pk=id)
        try:
            category.delete()
            return Response ({},status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({} , status=status.HTTP_400_BAD_REQUEST)
    except Category.DoesNotExist:
        return Response ({},status=status.HTTP_404_NOT_FOUND)

@api_view(['PUT'])
def updateCategory(request , id):
    try:
        category = Category.objects.get(pk= id)
        serializer = CategoryModelSerializer(data= request.data , instance= category)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_202_ACCEPTED )
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
    except:
        return Response({} , status= status.HTTP_404_NOT_FOUND)