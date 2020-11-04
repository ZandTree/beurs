from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from .models import Customer,Employee

User = get_user_model()

# class PersonForm(forms.ModelForm):
#     class Meta:
#        fields = ('location','phone_number','add_form_number')  

# class CustomerForm(PersonForm):
class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('location','phone_number','add_phone_number')  
        

# class EmployeeForm(PersonForm):
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('location','phone_number','add_phone_number')  
          

     

        
    

