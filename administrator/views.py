from itertools import product
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from administrator.serializer import *

from .form import *
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
            elif obj.usertype == 'supplyco':
              return render(request,'supplyco/supplycohome/supplycohome.html')
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
    # def post(self,request,pk):
    #     c= 
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
class stockbooking(View):
    def get(self,request):
        obj=shopBookingtable.objects.all()
        return render(request,'ration shop/viewbooking/viewbooking.html',{'obj':obj}) 
class productbooking(View):
    def get(self,request):
        obj=supplycoBookingtable.objects.all()
        return render(request,'supplyco/view booking/viewbooking.html',{'obj':obj})     
class addandmanageproduct(View):
    def get(self,request):
        c=producttable.objects.all()
        return render(request,'supplyco/add&manageproduct/addandmanageproduct.html',{'a':c}) 
class addproduct(View):
    def get(self,request):
        c=producttable.objects.all()
        return render(request,'supplyco/add&manageproduct/addproduct.html',{'a':c})
    def post(seif,request):
        form=productForm(request.POST, request.FILES) 
        if form.is_valid():
            f=form.save(commit=False)
            obj = supplycoprofile.objects.get(LOGINID=request.session['user_id'])
            f.SUPPLYCO=obj
            f.save()
            return HttpResponse('''<script>alert("added");window.location="/addandmanageproduct"</script>''')
class editproduct(View):
    def get(self,request,productid):
        c=producttable.objects.get(id=productid)
        return render(request,'supplyco/add&manageproduct/editproduct.html',{'a':c})  
    def post(seif,request, productid):
        c=producttable.objects.get(id=productid)

        form=StockForm(request.POST, request.FILES, instance=c) 
        if form.is_valid():
            form.save()
        
            return HttpResponse('''<script>alert("edited");window.location="/addandmanageproduct"</script>''')
class deleteproduct(View):
    def get(self,request,productid):
        c=producttable.objects.get(id=productid)
        c.delete()
        return HttpResponse('''<script>alert("deleted");window.location="/addandmanageproduct"</script>''')                    
class managenotification(View):
    def get(self,request):
        return render(request,'supplyco/manage notifications/managenotification.html')
    def post(seif,request):
        form=notificationForm(request.POST, request.FILES) 
        if form.is_valid():
            form.save()
            return HttpResponse('''<script>alert("sended");window.location="/managenotification"</script>''')
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
class viewproduct(View):
    def get(self,request,bookingid):
        obj=supplycoBookingtable.objects.get(id=bookingid)
        return render(request,'supplyco/viewproduct/viewproduct.html',{'a':obj})    


# ////////////////////////////////////////////////// API ///////////////////////////////////////////////////////////

from django.contrib.auth.hashers import make_password

class SignupApi(APIView):
    def post(self, request):
        print("#########", request.data)
        
        # Initialize serializers
        user_serializer = UserSerializer(data=request.data)
        login_serializer = LoginSerializer(data=request.data)

        # Validate both serializers
        user_valid = user_serializer.is_valid()
        login_valid = login_serializer.is_valid()

        if user_valid and login_valid:
            print("&&&&&&&&&&&&&&")
            

            # Save the login profile
            login_profile = login_serializer.save(usertype='USER')

            # Save the user profile with the login profile reference
            user_serializer.save(LOGINID=login_profile)

            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        
        # Return validation errors if any
        return Response({
            'login_error': login_serializer.errors if not login_valid else None,
            'user_error': user_serializer.errors if not user_valid else None
        }, status=status.HTTP_400_BAD_REQUEST)
    


class LoginApi(APIView):
    def post(self, request):
        print("###################")
        response_dict = {}

        # Get data from the request
        username = request.data.get("username")
        password = request.data.get("password")
        print(username)
        print(password)
        # Validate input
        if not username or not password:
            response_dict["message"] = "failed"
            return Response(response_dict, status=status.HTTP_400_BAD_REQUEST)

        # Fetch the user from LoginTable
        t_user = LoginTable.objects.filter(username=username).first()

        if not t_user:
            response_dict["message"] = "failed"
            return Response(response_dict, status=status.HTTP_401_UNAUTHORIZED)

        # # Check password using check_password
        # if not check_password(password, t_user.password):
        #     response_dict["message"] = "failed"
        #     return Response(response_dict, status=status.HTTP_401_UNAUTHORIZED)

        # Successful login response
        response_dict["message"] = "success"
        response_dict["login_id"] = t_user.id

        return Response(response_dict, status=status.HTTP_200_OK)


class ProfileApi(APIView):
    def get(self,request, p_id):
        print("@@@@@@@@@@@@@@@@@", p_id)
        profile = usertable.objects.filter(LOGINID_id=p_id)
        profile_serializer = ProfileSerializer(profile, many = True)
        print("$$$$$$$$$$$$$",profile_serializer.data)
        return Response(profile_serializer.data, status=status.HTTP_200_OK) 

class EditprofileApi(APIView):
    def get(self,request):
        profile = usertable.objects.all()
        profile_serializer = UserSerializer(profile, many = True)
        return Response(profile_serializer.data) 
class FeedbackApi(APIView):
    def get(self,request):
        feedback = feedbacktable.objects.all()
        feedback_serializer = FeedbackSerializer(feedback, many = True)
        return Response(feedback_serializer.data) 
    
class ViewstockApi(APIView):
    def get(self,request):
        stock = stocktable.objects.all()
        stock_serializer = ViewstockSerializer(stock, many = True)
        return Response(stock_serializer.data)       
    
class StockApi(APIView):
    def get(self,request):
        stock = stocktable.objects.all()
        stock_serializer = stockSerializer(stock, many = True)
        return Response(stock_serializer.data)       


class ShoporderApi(APIView):
    def get(self,request):
        stock = shopBookingtable.objects.all()
        stock_serializer = ShopordersSerializer(stock, many = True)
        return Response(stock_serializer.data)     

class ShoptimeApi(APIView):
    def get(self,request):
        stock = Shopprofile.objects.all()
        stock_serializer = ShoptimeSerializer(stock, many = True)
        return Response(stock_serializer.data) 

class ViewproductApi(APIView):
    def get(self,request):
        stock = producttable.objects.all()
        stock_serializer = ViewproductSerializer(stock, many = True)
        return Response(stock_serializer.data) 

class ProductApi(APIView):
    def get(self,request):
        stock = producttable.objects.all()
        stock_serializer = ProductSerializer(stock, many = True)
        return Response(stock_serializer.data)  
    

class SupplycoordersApi(APIView):
    def get(self,request):
        stock = supplycoBookingtable.objects.all()
        stock_serializer = supplycoordersSerializer(stock, many = True)
        return Response(stock_serializer.data)     


class NotificatinsApi(APIView):
    def get(self,request):
        stock =notificationtable.objects.all()
        stock_serializer = NotificationsSerializer(stock, many = True)
        return Response(stock_serializer.data)   

               
           


     
