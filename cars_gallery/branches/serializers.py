from rest_framework import serializers
from .models import Branch
from cars.serializers import CarModelSerializer
from employees.serializer import EmpModelSerializer

class BranchModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class BranchSerializer(serializers.Serializer):
        id=serializers.IntegerField(read_only = True)
        name = serializers.CharField(max_length= 250 , allow_blank= False)
        address = serializers.CharField(max_length = 1000)
        phone = serializers.CharField(max_length=20)
        employees = serializers.CharField(max_length = 250 , source = 'employees.name')
        cars = serializers.CharField(max_length = 250 , source = 'cars.name')

class SearchSerializer(serializers.Serializer):
    name = serializers.CharField(max_length= 250)


class BranchSerializer2(serializers.Serializer):
    name = serializers.CharField(max_length= 250)
    cars = CarModelSerializer(many = True)
    employees = EmpModelSerializer(many = True)
