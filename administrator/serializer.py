from administrator.models import LoginTable, Shopprofile, feedbacktable, notificationtable, producttable, shopBookingtable, stocktable, supplycoBookingtable, usertable
from rest_framework.serializers import ModelSerializer

class ProfileSerializer(ModelSerializer):

    class Meta:
        model=usertable
        fields=['name','phone','email']


class FeedbackSerializer(ModelSerializer):

    class Meta:
        model=feedbacktable
        fields=['user','feedback','date']

class LoginSerializer(ModelSerializer):

    class Meta:
        model=LoginTable
        fields=['username','password']
      
class UserSerializer(ModelSerializer):

    class Meta:
        model=usertable
        fields=['name','phone','email'] 


class ViewstockSerializer(ModelSerializer):

    class Meta:
        model=stocktable
        fields=['stockid','name','image','price','quantity']

class stockSerializer(ModelSerializer):

    class Meta:
        model=stocktable
        fields=['username','password']

class ShopordersSerializer(ModelSerializer):

    class Meta:
        model=shopBookingtable
        fields=['date']   

class ShoptimeSerializer(ModelSerializer):

    class Meta:
        model=Shopprofile
        fields=['openningtime','closingtime']   

class ViewproductSerializer(ModelSerializer):

    class Meta:
        model=producttable
        fields=['productid','name','image','description','price','marketprice','quantity']

class ProductSerializer(ModelSerializer):

    class Meta:
        model=producttable
        fields=['productid','name','image','description','price','marketprice','quantity']

class supplycoordersSerializer(ModelSerializer):

    class Meta:
        model=supplycoBookingtable
        fields=['date']                 

class NotificationsSerializer(ModelSerializer):

    class Meta:
        model=notificationtable
        fields=['notification','datetime']          




                
