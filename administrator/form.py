from django.forms import ModelForm
from.models import*

class StockForm(ModelForm):
    class Meta:
        model=stocktable
        fields=['stockid','name','image','price','quantity']
class productForm(ModelForm):
    class Meta:
        model=producttable
        fields=['productid','name','image','price','marketprice','quantity']     
class notificationForm(ModelForm):
    class Meta:
        model=notificationtable
        fields=['notification']           