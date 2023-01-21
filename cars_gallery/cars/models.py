from django.db import models
from categories.models import Category
from branches.models import Branch

# Create your models here.
class Car(models.Model):
    name = models.CharField(max_length= 250)
    arabic_name = models.CharField(max_length= 250,null=True,blank=True)
    price= models.DecimalField(max_digits= 20, decimal_places= 4, default= 0)
    color = models.CharField(max_length= 50)
    image = models.ImageField(null=True,blank= True ,upload_to= "images/")
    category = models.ForeignKey(Category, on_delete= models.DO_NOTHING , related_name= 'cars' , related_query_name= 'car')
    branch = models.ForeignKey(Branch, on_delete= models.DO_NOTHING,related_name= 'cars', related_query_name= 'car')

    class Meta:
        db_table= 'cars'
    def __str__(self):
        return self.name