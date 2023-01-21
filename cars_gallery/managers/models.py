from django.db import models
from branches.models import Branch
# Create your models here.
class Manager(models.Model):
    name = models.CharField(max_length= 250)
    salary= models.DecimalField(max_digits= 20, decimal_places= 4, default= 0)
    phone = models.CharField(max_length=20)
    branch = models.ForeignKey(Branch, on_delete= models.DO_NOTHING)

    class Meta:
        db_table= 'managers'

    def __str__(self):
        return self.name