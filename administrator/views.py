from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View

from .form import StockForm
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
            elif obj.usertype == 'shop':
              return render(request,'ration shop/rationhome/rationhome.html')
            else:
              return HttpResponse('''<script>alert("invalid username and password");window.location="/adminlogin"</script>''')

        except LoginTable.DoesNotExist:
            return HttpResponse('''<script>alert("invalid username and password");window.location="/adminlogin"</script>''')


        return redirect('login')


class verifyshop(View):    
    def get(self,request): 
        c=Shopprofile.objects.all()
        return render(request,'administrator/verifyshop/verifyshop.html',{'a':c})
    
class approve_shop(View):
    def get(self,request,login_id):
        obj=LoginTable.objects.get(id=login_id)
        obj.usertype="shop"
        obj.save()
        return HttpResponse('''<script>alert("accept");window.location="/verifyshop"</script>''')
class reject_shop(View):
    def get(self,request,login_id):
        obj=LoginTable.objects.get(id=login_id)
        obj.usertype="reject"
        obj.save()
        return HttpResponse('''<script>alert("reject");window.location="/verifyshop"</script>''')
class complaint(View):
    def get(self,request):
        c=complainttable.objects.all()
        return render(request,'administrator/view complaint & reply/complaint.html',{'a':c})
class complaintreply(View):
    def get(self,request,pk):
        c=complainttable.objects.get(pk=pk)
        return render(request,'administrator/view complaint & reply/complaintreply.html',{'a':c})   
class feedback(View):
    def get(self,request):
        c=feedbacktable.objects.all()
        return render(request,'administrator/view feedback/feedback.html',{'a':c})                                             
class addandupdatestock(View):
    def get(self,request):
        c=stocktable.objects.all()
        return render(request,'ration shop/addandupdate/addandupdatestock.html',{'a':c})
class addstock(View):
    def get(self,request):
        c=stocktable.objects.all()
        return render(request,'ration shop/addandupdate/addstock.html',{'a':c}) 
    def post(seif,request):
        form=StockForm(request.POST, request.FILES) 
        if form.is_valid():
            f=form.save(commit=False)
            obj = Shopprofile.objects.get(LOGINID=request.session['user_id'])
            f.SHOP=obj
            f.save()
            return HttpResponse('''<script>alert("added");window.location="/addandupdatestock"</script>''')
class editstock(View):
    def get(self,request,stock_id):
        c=stocktable.objects.get(id=stock_id)
        return render(request,'ration shop/addandupdate/editstock.html',{'a':c})
    def post(seif,request, stock_id):
        c=stocktable.objects.get(id=stock_id)

        form=StockForm(request.POST, request.FILES, instance=c) 
        if form.is_valid():
            form.save()
        
            return HttpResponse('''<script>alert("added");window.location="/addandupdatestock"</script>''')   
class deletestock(View):
    def get(self,request,stock_id):
        c=stocktable.objects.get(id=stock_id)
        c.delete()
        return HttpResponse('''<script>alert("deleted");window.location="/addandupdatestock"</script>''')


class addandupdate(View):
    def get(self,request):
        return render(request,'ration shop/addandupdate/editstock.html')    
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
        obj=Shopprofile.objects.all()
        return render(request,'ration shop/shopopeningandclosingstatus/shopopeningandclosingstatus.html',{'obj':obj})                         
class viewbooking(View):
    def get(self,request):
        obj=shopBookingtable.objects.all()
        return render(request,'ration shop/viewbooking/viewbooking.html',{'obj':obj}) 
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
        c=usertable.objects.all()
        return render(request,'administrator/view user/viewusers.html',{'a':c}) 
class supplycohome(View):
    def get(self,request):
        return render(request,'supplyco/supplycohome/supplycohome.html')
class addandmanagesupplyco(View):
    def get(self,request):
        c=supplycoprofile.objects.all()
        return render(request,'administrator/addandmanagesupplyco/addandmanagesupplyco.html',{'a':c})
class approve_supplyco(View):
    def get(self,request,login_id):
        obj=LoginTable.objects.get(id=login_id)
        obj.usertype="supplyco"
        obj.save()
        return HttpResponse('''<script>alert("accept");window.location="/addandmanagesupplyco"</script>''')
class reject_supplyco(View):
    def get(self,request,login_id):
        obj=LoginTable.objects.get(id=login_id)
        obj.usertype="reject"
        obj.save()
        return HttpResponse('''<script>alert("reject");window.location="/addandmanagesupplyco"</script>''')
