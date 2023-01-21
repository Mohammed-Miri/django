from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Car
from categories.models import Category

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'


class CarSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length = 250)
    price= serializers.DecimalField(max_digits= 20, decimal_places= 4, default= 0)
    color = serializers.CharField(max_length = 1000)
    image = serializers.ImageField()
    category = serializers.PrimaryKeyRelatedField(queryset= Category.objects.all() , write_only = True)
    category_name = serializers.CharField(max_length = 250 , source = 'category.name' , read_only = True)
    category_id = serializers.IntegerField(source = 'category.id' , read_only = True)
    
    
    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name' , instance.name)
        instance.save()
        return instance
    
class CarSearchSerializer(serializers.Serializer):
    name = serializers.CharField(max_length= 250 , allow_blank= False)
    
class CarSearchSerializer2(serializers.Serializer):
    name = serializers.CharField(max_length= 250 , allow_blank= False)
    price1= serializers.DecimalField(max_digits= 20, decimal_places= 4, default= 0)
    price2= serializers.DecimalField(max_digits= 20, decimal_places= 4, default= 0)
    category = serializers.PrimaryKeyRelatedField(queryset= Category.objects.all())

class CarSerializer2(serializers.Serializer):
    id=serializers.IntegerField(read_only = True)
    name = serializers.CharField(max_length = 250 , allow_blank = True)
    arabic_name = serializers.CharField(max_length = 250 , allow_blank = True)
    price= serializers.DecimalField(max_digits= 20, decimal_places= 4, default= 0)
    category = serializers.PrimaryKeyRelatedField(queryset= Category.objects.all() , write_only = True)
