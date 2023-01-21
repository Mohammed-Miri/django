from django.db import models
from cars.models import Car
from sections.models import Section
from branches.models import Branch


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length= 250)
    salary= models.DecimalField(max_digits= 20, decimal_places= 4, default= 0)
    job = models.CharField(max_length= 250)
    phone = models.CharField(max_length=20)
    dept = models.ForeignKey(Section, on_delete= models.DO_NOTHING)
    branch = models.ForeignKey(Branch, on_delete= models.DO_NOTHING,related_name= 'employees', related_query_name= 'employee')

    class Meta:
        db_table= 'employees'

    def __str__(self):
        return self.name