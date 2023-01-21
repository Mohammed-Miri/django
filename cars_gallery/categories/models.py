from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length= 250)
    description = models.CharField(max_length= 250 , null= True , blank= True)
    class Meta:
        db_table= 'categories'
    
    def __str__(self):
        return self.name