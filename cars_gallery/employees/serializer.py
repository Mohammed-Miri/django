from rest_framework import serializers
from .models import Employee


class EmpModelSerializer(serializers.ModelSerializer):
        class Meta:
            model = Employee
            fields = '__all__'
            
class EmpSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only = True)
    # name = serializers.CharField(max_length = 250)
    # salary= serializers.DecimalField(max_digits= 20, decimal_places= 4, default= 0)
    # job = serializers.CharField(max_length = 250)
    # phone = serializers.CharField(max_length=20)
    # dept = serializers.PrimaryKeyRelatedField(queryset= Section.objects.all() , write_only = True)
