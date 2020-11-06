from django.views.generic import CreateView,TemplateView
from django.contrib.auth import get_user_model
# from django.shortcuts
from django.http import JsonResponse  
from .forms import *

User = get_user_model()

class CustomerRegister(CreateView):
    form_class = CustomerForm
    success_url = 'customer/customer-dashboard.html'
    template_name = 'customer/customer-form.html'

    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        self.request.user.is_customer = True
        self.request.user.save()        
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {"msg": "Submission successful"}        
            return JsonResponse({"data":data})
        else:
            return response 

    def form_invalid(self,form): 
        """ If form is invalid return status 400 array of errors """ 
        response = super().form_invalid(form)        
        msg = "something went wrong"        
        errors = form.errors.as_json() # string
        return JsonResponse ({"msg":msg,"errors":errors},status = 400)   
               
class CustomerDashboard(TemplateView):
    template_name = 'customer/customer-dashboard.html'

class EmployeeRegister(CreateView):
    form_class = EmployeeForm
    success_url = 'employee/employee-dashboard.html'
    template_name = 'employee/employee-form.html' 

    def form_valid(self,form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        self.request.user.is_employee = True
        self.request.user.save()        
        response = super().form_valid(form)       
        if self.request.is_ajax():
            data = {"msg": "Submission successful"}        
            return JsonResponse({"data":data})
        else:
            return response 
    def form_invalid(self,form): 
        """ If form is invalid return status 400 array of errors """ 
        response = super().form_invalid(form)         
        msg = "something went wrong"        
        errors = form.errors.as_json() # string
        return JsonResponse ({"msg":msg,"errors":errors},status = 400)         

    

 
    

class EmployeeDashboard(TemplateView):
    template_name = 'employee/employee-dashboard.html'


     

       

    

   