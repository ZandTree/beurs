#  https://djangotricks.blogspot.com/search/label/Django%20REST%20Framework (about upload drf)
import os
import sys
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from .utils import upload_to
import uuid


class User(AbstractUser):
    """ 
    username + email for signup; email for login;
    user should choose at the moment of signUp one of two options: 
    is_customer or is employee;
    admin/staff members could keep default values;
    """
    username = models.CharField(_("Username"),unique=True,max_length=120)
    email = models.EmailField(_("Email"),unique=True)
    avatar = models.ImageField(_("Avatar"), upload_to=upload_to, blank=True)
    phone_number = models.CharField(max_length=20,blank=True)
    is_customer = models.BooleanField(_("customer status"),default=False)
    is_employee = models.BooleanField(_("employee status"),default=False)
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

class Customer(models.Model):
    """ extra attr unid to display in public space"""
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    unid = models.UUIDField(max_length=255, default = uuid.uuid4,editable = False)
    
    def __str__(self):
        return f'Customer {self.user.username}'    
    

class Employee(models.Model):
    """ extra attr unid to display in public space"""
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    location = models.CharField(max_length=250,default='') 
    unid = models.UUIDField(max_length=255, default = uuid.uuid4,editable = False)
    
    def __str__(self):
        return f"Employee {self.user.username}"