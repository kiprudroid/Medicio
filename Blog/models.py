from django.db import models

# Create your models here.
class Users(models.Model):
    fullname = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)
    email = models.EmailField()
    password = models.CharField(max_length = 30)
    age = models.IntegerField(null = True)
    yearOfBirth = models.DateField(null = True)

    def __str__(self) -> str:
        return self.username
    
class Products(models.Model):
    productName = models.CharField(max_length = 200)
    productQuantity = models.IntegerField(null = True)
    price = models.CharField(max_length = 200)
    def __str__(self) -> str:
        return self.productName

