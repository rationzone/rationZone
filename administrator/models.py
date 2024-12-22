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
    phone=models.BigIntegerField(null=True,blank=True)
    openningtime=models.CharField(max_length=100,null=True,blank=True)

class Bookingtable(models.Model):
    customerid=models.CharField(max_length=100,null=True,blank=True)
    bookingtime=models.CharField(max_length=100,null=True,blank=True)
    productid=models.CharField(max_length=100,null=True,blank=True)
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)

class complainttable(models.Model):
    customerid=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    complaint=models.CharField(max_length=100,null=True,blank=True)
    datetime=models.CharField(max_length=100,null=True,blank=True)
    
class notificationtable(models.Model): 
    notification=models.CharField(max_length=100,null=True,blank=True)
    datetime=models.CharField(max_length=100,null=True,blank=True)

class producttable(models.Model):
    productid=models.CharField(max_length=100,null=True,blank=True)
    price=models.CharField(max_length=100,null=True,blank=True)
    quantity=models.CharField(max_length=100,null=True,blank=True)
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)

class usertable(models.Model):
    userid=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    
class feedbacktable(models.Model):
    userid=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)
    feedback=models.CharField(max_length=100,null=True,blank=True)
    datetime=models.CharField(max_length=100,null=True,blank=True)


      