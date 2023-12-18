from django.db import models

# Create your models here.
class User(models.Model):
    fname=models.TextField()
    lname=models.TextField()
    email=models.EmailField(max_length=254)
    pwd=models.TextField()
    gender=models.TextField()
    addr=models.TextField()
    
    def __str__(self) :
        return self.email
    