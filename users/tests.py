from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Employee,Customer

User  = get_user_model()

class UsersManagersTests(TestCase):

    def test_create_user(self):
        """ check that user has required not default fields AND is NOT superuser/staff"""
        user = User.objects.create_user(username="zoo",email='zoo@mail.com', password='123abc')
        self.assertEqual(user.email, 'zoo@mail.com')
        self.assertEqual(user.username, 'zoo')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_customer)
        self.assertFalse(user.is_employee)
        self.assertFalse(user.is_superuser)       
        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(username='')
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(username='',email='', password="foo")

    def test_create_user_shell_or_adminpanel(self):
        """ 
        create user via adminpanel or shell with attrs is_customer/is_employee = default
        """        
        user = User.objects.create_user(username="zoo",email='zoo@mail.com', password='123abc')
        self.assertFalse(user.is_customer)
        self.assertFalse(user.is_employee) 
                 

    def test_create_superuser(self):        
        admin_user = User.objects.create_superuser('tata','tata@mail.com', 'foo')
        self.assertEqual(admin_user.username, 'tata')
        self.assertEqual(admin_user.email, 'tata@mail.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)       
        self.assertTrue(admin_user.is_superuser)
        with self.assertRaises(ValueError):
            User.objects.create_superuser(username='bird',email='bird@mail.com', password='foo', 
            is_superuser=False)
   
class CustomerTesCase(TestCase):  
    """ create new customer and change user 'is_customer' True'  """  
    def setUp(self):
        self.user = User.objects.create(
            username = "monkey", email = "zaza@mail.com")
        self.customer = Customer.objects.create(user=self.user)          
        
    def test_customer_attrs(self):
        self.assertTrue(hasattr(self.user,'customer'))   
        self.assertTrue(hasattr(self.customer,'user')) 
        self.assertEqual(self.customer.user.username, 'monkey')
        self.assertTrue(self.user.is_customer,True) 

class EmployeeTesCase(TestCase):  
    def setUp(self):
        """ create new employee and change user 'is_employee' True 
        """  
        self.user = User.objects.create(
            username = "giraf", email = "foo@mail.com", is_employee = True
            )
        self.employee = Employee.objects.create(user=self.user)          
        

    def test_employee_attrs(self):
        self.assertTrue(hasattr(self.user,'employee'))   
        self.assertTrue(hasattr(self.employee,'user')) 
        self.assertEqual(self.employee.user.username, 'giraf') 
        self.assertTrue(self.user.is_employee,True)
            
       
               

    
 
        
        