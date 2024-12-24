from django.forms import ModelForm
from.models import*

class StockForm(ModelForm):
    class Meta:
        model=stocktable
        fields=['stockid','name','image','price','quantity']