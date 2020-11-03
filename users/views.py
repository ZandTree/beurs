from django.views.generic import RedirectView,TemplateView
from django.contrib.auth import get_user_model
User = get_user_model()
# from django.contrib.auth.forms import UserCreationForm
# from .forms import *

class CustomerRegister(RedirectView):
    pattern_name = 'users:customer-dashboard'    
    def get_redirect_url(self,*args,**kwargs):
        # some logic here
        # user gets is_customer True
        return super().get_redirect_url(*args,**kwargs) 

class CustomerDashboard(TemplateView):
    template_name = 'customer/customer-dashboard.html'

class EmployeeDashboard(RedirectView):
    pattern_name = 'users:employee-dashboard'    
    def get_redirect_url(self,*args,**kwargs):
        # some logic here
        # user gets is_employee True
        return super().get_redirect_url(*args,**kwargs)

class EmployeeRegister(TemplateView):
    template_name = 'employee/employee-dashboard.html'


     

    

   