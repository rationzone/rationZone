from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from .models import *
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
    def post(self,request):
        # get the username and password from the POST request
        username=request.POST.get('username')
        password=request.POST.get('password')
        print(username,password)

        try:
            obj=LoginTable.objects.get(username=username,password=password)
            request.session['user_id']=obj.id
            print(username,password,obj.id,obj.usertype)

            if obj.usertype == 'admin':
              return render(request,'administrator/add&managesupplyco/adminhome.html')
            elif obj.usertype == 'user':
              return render(request,'ration shop/rationhome/rationhome.html')
            else:
              return HttpResponse('''<script>alert("invalid username and password");window.location="/adminlogin"</script>''')

        except LoginTable.DoesNotExist:
            return HttpResponse('''<script>alert("invalid username and password");window.location="/adminlogin"</script>''')


        return redirect('login')


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
         return render(request,'ration shop/addandupdate/addandupdate.html')
class deliverystatus(View):
    def get(self,request):
         return render(request,'ration shop/delivery status/deliverystatus.html')
class rationhome(View):
    def get(self,request):
         return render(request,'ration shop/rationhome/rationhome.html')
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
         return render(request,'administrator/view user/viewusers.html')                         
class supplycohome(View):
    def get(self,request):
         return render(request,'supplyco/supplycohome/supplycohome.html')
class addandmanagesupplyco(View):
    def get(self,request):
         return render(request,'supplyco/addandmanagesupplyco/addandmanagesupplyco.html')

