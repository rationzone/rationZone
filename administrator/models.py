from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=30,null=True,blank=True)
    usertype=models.CharField(max_length=30,null=True,blank=True)

class Shopprofile(models.Model):
    shopname=models.CharField(max_length=100,null=True,blank=True)
    owner=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    phone=models.BigIntegerField(null=True,blank=True)
    openningtime=models.TimeField(null=True,blank=True)
    closingtime=models.TimeField(null=True,blank=True)
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)

class supplycoprofile(models.Model):
    supplyid=models.CharField(max_length=100,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    phone=models.BigIntegerField(null=True,blank=True)
    openningtime=models.TimeField(null=True,blank=True)
    closingtime=models.TimeField(null=True,blank=True)
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)    


class usertable(models.Model):
    userid=models.CharField(max_length=100,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    phone=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    address=models.CharField(max_length=100,null=True,blank=True)
    LOGINID=models.ForeignKey(LoginTable,on_delete=models.CASCADE,null=True,blank=True)


class complainttable(models.Model):
    USER=models.ForeignKey(usertable,on_delete=models.CASCADE,null=True,blank=True)
    complaint=models.CharField(max_length=100,null=True,blank=True)
    datetime=models.DateField(null=True,blank=True)
    
class notificationtable(models.Model): 
    notification=models.CharField(max_length=100,null=True,blank=True)
    datetime=models.DateField(null=True,blank=True)

class producttable(models.Model):
    productid=models.CharField(max_length=100,null=True,blank=True)
    name=models.CharField(max_length=100,null=True,blank=True)
    image=models.FileField()
    description=models.CharField(max_length=200,null=True,blank=True)
    price=models.FloatField(null=True,blank=True)
    quantity=models.CharField(max_length=100,null=True,blank=True)

class Bookingtable(models.Model):
    date=models.DateTimeField(null=True,blank=True)
    PRODUCT=models.ForeignKey(producttable,on_delete=models.CASCADE,null=True,blank=True)
    USERID=models.ForeignKey(usertable,on_delete=models.CASCADE,null=True,blank=True)
    STATUS=models.CharField(max_length=100,null=True,blank=True)

    
class feedbacktable(models.Model):
    user=models.ForeignKey(usertable,on_delete=models.CASCADE,null=True,blank=True)
    feedback=models.CharField(max_length=400,null=True,blank=True)
    date=models.DateField(null=True,blank=True)


      