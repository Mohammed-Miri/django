from django.db import models
from managers.models import Manager
# Create your models here.
class Section(models.Model):
    name = models.CharField(max_length= 250)
    manager = models.OneToOneField(Manager , on_delete= models.DO_NOTHING)
    
    class Meta:
        db_table= 'sections'

    def __str__(self):
        return self.name