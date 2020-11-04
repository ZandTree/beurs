from django.views.generic import RedirectView,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from django.contrib.auth import get_user_model
User = get_user_model()
# from django.contrib.auth.forms import UserCreationForm
# from .forms import *

class CustomerRegister(RedirectView):
    pattern_name = 'users:customer-dashboard' 
    http_method_names = ['post'] 

    def post(self, request, *args, **kwargs):
        print("inside post")
        user = request.user
        user.is_customer = True
        user.save()
        return super().post(request, *args, **kwargs)
        
    def get_redirect_url(self,*args,**kwargs):
        print("inside redirect")
        messages.success(
#                 self.request,
#                 "You're now a member of <b>{}</b>!".format(community.name)
#             )
        return super().get_redirect_url(*args,**kwargs) 

class CustomerDashboard(TemplateView):
    template_name = 'customer/customer-dashboard.html'

class EmployeeRegister(RedirectView):
    pattern_name = 'users:employee-dashboard' 
    http_method_names = ['post']  

    def post(self, request, *args, **kwargs):
        print("inside post")
        user = request.user
        user.is_customer = True
        user.save()
        return super().post(request, *args, **kwargs)   
    def get_redirect_url(self,*args,**kwargs):
        user = self.request.user
        user.is_employee = True
        user.save()       
        return super().get_redirect_url(*args,**kwargs)

class EmployeeDashboard(TemplateView):
    template_name = 'employee/employee-dashboard.html'


     

    

   