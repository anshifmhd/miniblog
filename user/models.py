from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    

class Account(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    type = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Blog(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.CharField(max_length=10000)
    image = models.ImageField(upload_to='blogs/')
    user = models.ForeignKey(Account, on_delete=models.CASCADE, null= True)



class Comments(models.Model):
    comments = models.CharField(max_length=3000)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True)