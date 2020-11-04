from django.views.generic import CreateView,TemplateView
from django.contrib.auth import get_user_model
from .forms import *

User = get_user_model()

class CustomerRegister(CreateView):
    form_class = CustomerForm
    success_url = '/'
    template_name = 'customer/customer-form.html'
    

class CustomerDashboard(TemplateView):
    template_name = 'customer/customer-dashboard.html'

class EmployeeRegister(CreateView):
    form_class = EmployeeForm
    success_url = '/'
    template_name = 'employee/employee-form.html'    
    

class EmployeeDashboard(TemplateView):
    template_name = 'employee/employee-dashboard.html'


     

    

   