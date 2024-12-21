
from django.urls import path
from .views import *

urlpatterns = [
    path('adminhome',adminhome.as_view(),name='adminhome'),
    path('digitalcard',digitalcard.as_view(),name='digitalcard'),
    path('adminlogin',adminlogin.as_view(),name='adminlogin'),
    path('verifyshop',verifyshop.as_view(),name='verifyshop'),
    path('complaint',complaint.as_view(),name='complaint'),
    path('feedback',feedback.as_view(),name='feedback'),
    path('viewuser',viewuser.as_view(),name='viewuser'),
    path('deliverystatus',deliverystatus.as_view(),name='deliverystatus'),
    path('rationshoplogin',rationshoplogin.as_view(),name='rationshoplogin'),
    path('shopregistration',shopregistration.as_view(),name='shopregistration'),
    path('shopopeningandclosingstatus',shopopeningandclosingstatus.as_view(),name='shopopeningandclosingstatus'),
    path('viewbooking',viewbooking.as_view(),name='viewbooking'),
    path('addandmanageproduct',addandmanageproduct.as_view(),name='addandmanageproduct'),
    path('managenotification',managenotification.as_view(),name='managenotification'),
    path('supplycologin',supplycologin.as_view(),name='supplycologin'),
    path('viewusers',viewusers.as_view(),name='viewusers'),
]
