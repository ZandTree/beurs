from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer as DjoserUserSer
from rest_framework import serializers as ser
from users.models import Customer,Employee

User = get_user_model()


#custom part for djoser module(see settings for built-in)
class UserCreateSerializer(DjoserUserSer):
   class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name','is_customer','is_employee']

class CustomerSerializer(ser.ModelSerializer):
    user =  UserCreateSerializer()
    name = ser.CharField(source='user.username', read_only=True)
    unid = ser.UUIDField(format="hex_verbose",read_only=True)
    class Meta:
        model = Customer
        fields = ('user_id','unid','name','user') 

class EmployeeSerializer(ser.ModelSerializer):
    user =  UserCreateSerializer()
    name = ser.CharField(source='user.username', read_only=True)
    unid = ser.UUIDField(format="hex_verbose",read_only=True)
    class Meta:
        model = Employee
        fields = ('user_id','unid','name','user') 
      
        