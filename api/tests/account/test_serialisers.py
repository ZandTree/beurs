from django.test import TestCase
from users.models import Customer, Employee
from api.account.serializers import CustomerSerializer, EmployeeSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers as ser
from django.urls import reverse

User = get_user_model()

class CustomerSerializerTesCase(TestCase):
    """Customer: compare expected and received data after ser-on"""
    def setUp(self):        
        self.user = User.objects.create(
            username="giraf",
            email="zoo@mail.com",
            is_customer=True
            )        
        self.customer = Customer.objects.last()
        
    def test_customer_serializer(self):      
        """ let op: not arr but dict"""     
        user_customer_serial = CustomerSerializer(self.customer).data
        expected_data = {
                "unid": str(self.customer.unid),            
                "user_id": self.user.id,                                 
                "name":self.user.username,
                "user":{
                    "username":self.user.username,
                    "email":self.user.email,
                    "first_name":"",
                    "last_name":"",                    
                    "is_customer":True,
                    "is_employee":False
                    
                }
            }           
        self.assertEqual(user_customer_serial, expected_data)

class EmployeeSerializerTesCase(TestCase):
    """Employee: compare expected and received data after ser-on"""
    def setUp(self):        
        self.user = User.objects.create(
            username="monkey",
            email="zaza@mail.com",
            is_employee=True
            )        
        self.employee = Employee.objects.last()
        
    def test_employee_serializer(self):      
        """ """     
        user_employee_serial = EmployeeSerializer(self.employee).data
        expected_data = {
                "unid": str(self.employee.unid),            
                "user_id": self.user.id,                                 
                "name":self.user.username,
                "user":{
                    "username":self.user.username,
                    "email":self.user.email,
                    "first_name":"",
                    "last_name":"",                    
                    "is_customer": False,
                    "is_employee":True
                    
                }
            }           
        self.assertEqual(user_employee_serial, expected_data)
