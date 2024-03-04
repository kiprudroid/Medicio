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
    
class Members(models.Model):
    username = models.CharField(max_length = 200)
    email = models.EmailField()
    password = models.CharField(max_length = 30)
    
    def __str__(self) -> str:
        return self.username

class Response(models.Model):
    fullname = models.CharField(max_length = 30)
    email = models.EmailField()
    subject = models.CharField(max_length = 100)
    message = models.TextField()

    def __str__(self) -> str:
        return self.fullname +'|-----------|'+ self.subject

class ImageModel(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    price = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title
