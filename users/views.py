from django.views.generic import CreateView,TemplateView
from django.contrib.auth import get_user_model
# from django.shortcuts
from django.http import JsonResponse  
from .forms import *

User = get_user_model()


class CustomerRegister(CreateView):
    form_class = CustomerForm
    success_url = '/'
    template_name = 'customer/customer-form.html'

    # def form_valid(self,form):
    #     print("form",form)
    #     self.object = form.save(commit=False)
    #     self.object.user = self.request.user
    #     self.object.save()
    #     return super().form_valid(form)

    def post(self,request,*args,**kwargs):
        form = CustomerForm(request.POST)
        user = request.user
        if form.is_valid():
            obj = form.save(commit=False) 
            obj.user = user
            obj.save()
            user.is_customer = True
            user.save()
            return JsonResponse({"ok":True})
        else:
            msg = "wrong"
            return JsonResponse({"resp":wrong})    

class CustomerDashboard(TemplateView):
    template_name = 'customer/customer-dashboard.html'

class EmployeeRegister(CreateView):
    form_class = EmployeeForm
    success_url = 'employee/employee-dashboard.html'
    template_name = 'employee/employee-form.html' 

    def post(self,request,*args,**kwargs):
        form = EmployeeForm(request.POST)
        user = request.user
        if form.is_valid():
            obj = form.save(commit=False) 
            obj.user = user
            obj.save()
            user.is_employee = True
            user.save()
            return JsonResponse({"resp":'ok'})
        else:
            msg = "he-he wrong"
            print("errors in form:", form.errors.as_json())
            errors = form.errors.as_json()
            if form.non_field_errors:
                non_field_errs = form.non_field_errors()

            return JsonResponse ({"msg":msg,"errors":errors,"non_field_errs":non_field_errs}) 

# errors
# ('{"location": [{"message": "This field is required.", "code": "required"}], '
#  '"phone_number": [{"message": "This field is required.", "code": '
#  '"required"}], "add_phone_number": [{"message": "This field is required.", '
#  '"code": "required"}]}')                 

    
    

class EmployeeDashboard(TemplateView):
    template_name = 'employee/employee-dashboard.html'


     

    

   