from django.db import models
from employees.models import Employee
from branches.models import Branch

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length= 250)
    address = models.CharField(max_length= 250)
    phone = models.CharField(max_length=20)
    branch = models.ForeignKey(Branch, on_delete= models.DO_NOTHING)

    class Meta:
        db_table= 'clients'

    def __str__(self):
        return self.name