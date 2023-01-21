from  django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    UserSerializer,
    UserSearchSerializer
)


@api_view(['POST'])
def createUser(request):
    serializer = UserSerializer(data= request.data)
    if serializer.is_valid():
        userData = serializer.data
        User.objects.create_user(username = userData['username'],email= userData['email'],password= userData['password'])
        return Response({} , status= status.HTTP_201_CREATED)
    return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)

@api_view(['delete'])
def deleteUserByName(request , name):
    try:
        user= User.objects.filter(username = name)
        try:
            user.delete()
            return Response ({},status=status.HTTP_204_NO_CONTENT)
        except:
            return Response({} , status=status.HTTP_400_BAD_REQUEST)
    except User.DoesNotExist:
        return Response ({},status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def updateUser(request , id):
    try:
        user = User.objects.get(pk= id)
        serializer = UserSerializer(data= request.data , instance= user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status= status.HTTP_202_ACCEPTED )
        return Response(serializer.errors , status= status.HTTP_400_BAD_REQUEST)
    except:
        return Response({} , status= status.HTTP_404_NOT_FOUND)