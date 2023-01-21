from rest_framework import serializers
from .models import Category

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'



class CategorySerializer(serializers.Serializer):
    name = serializers.CharField(max_length= 250 , allow_blank= False)
    

class CountCategory(serializers.Serializer):
    count= serializers.DecimalField(max_digits= 20, decimal_places= 4, default= 0)
