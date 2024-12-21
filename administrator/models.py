from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=30,null=True,blank=True)
    usertype=models.CharField(max_length=30,null=True,blank=True)

class Shopprofile(models.Model):
    shopname=models.CharField(max_length=100,null=True,blank=True)
    owner=models.CharField(max_length=100,null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    phone=models.BigIntegerField(max_length=100,null=True,blank=True)
    openningtime=models.CharField(max_length=100,null=True,blank=True)
    clossing
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)