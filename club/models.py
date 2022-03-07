from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class PythonType(models.Model):
    typename=models.CharField(max_length=255)
    typedescription=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.typename
    
    class Meta:
        db_table='pythontype'
        
class Product(models.Model):
    productname=models.CharField(max_length=255)
    producttype=models.ForeignKey(PythonType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    dataentered=models.DateField()
    price=models.DecimalField(max_digits=6,decimal_places=2)
    producturl=models.URLField()
    description=models.TextField()


    def __str__(self):
        return self.productname
    
    class Meta:
        db_table='product'
        
class Review(models.Model):
    title=models.CharField(max_length=255)
    user=models.CharField(max_length=255)
    reviewdate=models.DateField()
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    reviewtext=models.TextField()

    def __str__(self):
        return self.reviewtitle
    
    class Meta:
        db_table='review'
        