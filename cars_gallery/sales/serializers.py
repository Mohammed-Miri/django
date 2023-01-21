from rest_framework import serializers
from .models import Sale
from cars.models import Car
from employees.models import Employee
from employees.serializer import EmpModelSerializer
from clients.models import Client

class SaleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'


class TimeSerializer(serializers.Serializer):
    time1 = serializers.DateField()
    time2 = serializers.DateField(required=False)
    
class SaleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 250)
    
class SaleSerializer2(serializers.Serializer):
    name = serializers.CharField(max_length = 250)
    sale = SaleModelSerializer(many  = True)