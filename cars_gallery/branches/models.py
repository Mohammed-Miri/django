from django.db import models

# Create your models here.
class Branch(models.Model):
    name = models.CharField(max_length= 250)
    address = models.CharField(max_length= 250)
    phone = models.CharField(max_length=20)
    class Meta:
        db_table= 'branches'

    def __str__(self):
        return self.name