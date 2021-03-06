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
    location = forms.CharField(max_length=5)
    phone_number = forms.CharField(widget = forms.NumberInput)
    add_phone_number = forms.CharField(widget = forms.NumberInput,required=False)

    class Meta:
        model = Customer
        fields = ('designation','location','phone_number','add_phone_number')  
        

# class EmployeeForm(PersonForm):
class EmployeeForm(forms.ModelForm):
    phone_number = forms.CharField(widget = forms.NumberInput)
    add_phone_number = forms.CharField(widget = forms.NumberInput)

    class Meta:
        model = Employee
        fields = ('location','phone_number','add_phone_number')  
          

     

        
    

