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
    
class Blog(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.TextField()
    desc=models.TextField()
    posted=models.DateTimeField(auto_now_add=True)

    
    def __str__(self) :
        return self.title