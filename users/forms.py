from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db import transaction
from .models import Customer,Employee

User = get_user_model()


class CustomerCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = User
        fields = ('username','email','password1','password2','is_customer') 

    # let op:
    # user.is_customer in forms already (not in view) 
    # @transaction.atomic
    # def save(self,commit=False):
    #     user = super().save(commit=False)
    #     user.is_customer = True
    #     user.save()
    #     customer = Customer.objects.create(user=user)
    #     customer.save()
    #     return user    

class  CustomerChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','avatar','phone_number')
        fields = UserChangeForm.Meta.fields
    
    # @transaction.atomic
    # def save(self):
    #     user = super().save(commit=False)
    #     if self.cleaned_data.get('avatar') is not None:
    #         user.phone_number=self.cleaned_data.get('avatar') 
    #     if self.cleaned_data.get('phone_number') is not None:
    #         user.phone_number=self.cleaned_data.get('phone_number')        
    #     user.save()
    #     customer = Customer.objects.create(user=user)
    #     customer.save()
    #     return user

class EmployeeCreationForm(UserCreationForm):   
    class Meta(UserCreationForm.Meta):
        fields = ('username','email','password1','password2') 
        model = User
    # let op:
    # user.is_employee in forms already (not in view) 
    # @transaction.atomic
    # def save(self,commit=False):
    #     user = super().save(commit=False)
    #     user.is_employee = True
    #     user.save()
    #     employee = Employee.objects.create(user=user)
    #     employee.save()
    #     return user 
    


class  EmployeeChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username','avatar','phone_number')
        fields = UserChangeForm.Meta.fields
    
    
    # @transaction.atomic
    # def save(self,commit=False):
    #     user = super().save(commit=False)
    #     if self.cleaned_data.get('avatar') is not None:
    #         user.phone_number=self.cleaned_data.get('avatar') 
    #     if self.cleaned_data.get('phone_number') is not None:
    #         user.phone_number=self.cleaned_data.get('phone_number')        
    #     user.save()
    #     customer = Customer.objects.create(user=user)
    #     customer.save()
    #     return user        