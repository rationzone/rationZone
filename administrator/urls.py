
from django.urls import path
from .views import *

urlpatterns = [
    path('adminhome',adminhome.as_view(),name='adminhome'),
    path('digitalcard',digitalcard.as_view(),name='digitalcard'),
    path('',adminlogin.as_view(),name='adminlogin'),
    path('verifyshop',verifyshop.as_view(),name='verifyshop'),
    path('approve_shop/<int:login_id>',approve_shop.as_view(),name='approve_shop'),
    path('reject_shop/<int:login_id>',reject_shop.as_view(),name='reject_shop'),
    path('complaint',complaint.as_view(),name='complaint'),
    path('complaintreply/<int:pk>',complaintreply.as_view(),name='complaintreply'),
    path('feedback',feedback.as_view(),name='feedback'),
    path('deliverystatus',deliverystatus.as_view(),name='deliverystatus'),
    path('rationhome',rationhome.as_view(),name='rationhome'),
    path('addandupdatestock',addandupdatestock.as_view(),name='addandupdatestock'),
    path('addstock',addstock.as_view(),name='addstock'),
    path('editstock/<int:stock_id>',editstock.as_view(),name='editstock'),
    path('deletestock/<int:stock_id>',deletestock.as_view(),name='deletestock'),
    path('rationshoplogin',rationshoplogin.as_view(),name='rationshoplogin'),
    path('shopregistration',shopregistration.as_view(),name='shopregistration'),
    path('shopopeningandclosingstatus',shopopeningandclosingstatus.as_view(),name='shopopeningandclosingstatus'),
    path('viewbooking',viewbooking.as_view(),name='viewbooking'),
    path('addandmanageproduct',addandmanageproduct.as_view(),name='addandmanageproduct'),
    path('managenotification',managenotification.as_view(),name='managenotification'),
    path('supplycologin',supplycologin.as_view(),name='supplycologin'),
    path('viewusers',viewusers.as_view(),name='viewusers'),
    path('supplycohome',supplycohome.as_view(),name='supplycohome'),
    path('addandmanagesupplyco',addandmanagesupplyco.as_view(),name='addandmanagesupplyco'),
    path('approve_supplyco/<int:login_id>',approve_supplyco.as_view(),name='approve_supplyco'),
    path('reject_supplyco/<int:login_id>',reject_supplyco.as_view(),name='reject_supplyco'),
]
