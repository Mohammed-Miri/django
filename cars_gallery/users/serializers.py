from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only = True)
    username = serializers.CharField(max_length = 250 , validators = [UniqueValidator(queryset=User.objects.all())])
    email = serializers.EmailField(max_length = 250)
    password = serializers.CharField(max_length = 1000)


    def update(self, instance, validated_data):
        instance.username = validated_data.get('username' , instance.username)
        instance.save()
        return instance
    
class UserSearchSerializer(serializers.Serializer):
    name = serializers.CharField(max_length= 250 , allow_blank= False)    