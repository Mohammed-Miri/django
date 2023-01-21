from django.db import models
from clients.models import Client
from employees.models import Employee
from branches.models import Branch
from cars.models import Car

class Sale(models.Model):
    date= models.DateField()
    time= models.TimeField()
    client = models.ForeignKey(Client, on_delete= models.DO_NOTHING)
    employee = models.ForeignKey(Employee , on_delete= models.DO_NOTHING , related_name= 'sale',related_query_name='sales')
    car= models.ForeignKey(Car, on_delete= models.DO_NOTHING , blank= True , null= True)
    price= models.DecimalField(max_digits= 20, decimal_places= 4 , blank= True , null= True)
    branch = models.ForeignKey(Branch , on_delete= models.DO_NOTHING)
    class Meta:
        db_table= 'sales'
    # def __str__(self):
    #     return self.name