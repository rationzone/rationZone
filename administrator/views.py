from django.shortcuts import render
from django.views import View

# Create your views here.
class adminhome(View):
    def get(self,request):
        return render(request,'administrator/add&managesupplyco/adminhome.html')
class digitalcard(View):
    def get(self,request):
        return render(request,'administrator/digital card/digitalcard.html')
class adminlogin(View):
    def get(self,request):
        return render(request,'administrator/login/adminlogin.html')
class verifyshop(View):
    def get(self,request):
        return render(request,'administrator/verifyshop/verifyshop.html')
class complaint(View):
    def get(self,request):
         return render(request,'administrator/view complaint & reply/complaint.html')
class feedback(View):
    def get(self,request):
         return render(request,'administrator/view feedback/feedback.html')                     
class viewuser(View):
    def get(self,request):
         return render(request,'administrator/view user/viewuser.html')                         
class addandupdate(View):
    def get(self,request):
         return render(request,'ration shop/add & update stocks/addandupdate.html') 
class deliverystatus(View):
    def get(self,request):
         return render(request,'ration shop/delivery status/deliverystatus.html')   
class rationshoplogin(View):
    def get(self,request):
         return render(request,'ration shop/rationshoplogin/rationshoplogin.html')
class shopregistration(View):
    def get(self,request):
         return render(request,'ration shop/rationshopregistration/shopregistration.html')   
class shopopeningandclosingstatus(View):
    def get(self,request):
         return render(request,'ration shop/shopopeningandclosingstatus/shopopeningandclosingstatus.html')                         
class viewbooking(View):
    def get(self,request):
         return render(request,'ration shop/viewbooking/viewbooking.html') 
class addandmanageproduct(View):
    def get(self,request):
         return render(request,'supplyco/add&manageproduct/addandmanageproduct.html') 
class managenotification(View):
    def get(self,request):
         return render(request,'supplyco/manage notifications/managenotification.html')
class supplycologin(View):
    def get(self,request):
         return render(request,'supplyco/supplyco login/supplycologin.html')  
class viewusers(View):
    def get(self,request):
         return render(request,'supplyco/view users/viewusers.html')                         
     
