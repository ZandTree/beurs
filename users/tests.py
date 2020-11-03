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
            User.objects.create_superuser(
                username='bird',email='bird@mail.com', password='foo', is_superuser=False)

    def test_create_user_one_role(self):
        """ check for unique option by singup via site form: 
        here: user should be customer but not employee
        """       
        user_customer = User.objects.create_user(
            username = 'bird',
            email = 'bird@mail.com', 
            password = '12345abc',
            is_customer = True,
            is_employee = False
            )
        self.assertEqual(user_customer.username, 'bird')
        self.assertEqual(user_customer.email, 'bird@mail.com')
        self.assertFalse(hasattr(user_customer,'employee'))
        self.assertTrue(hasattr(user_customer,'customer'))

        with self.assertRaises(TypeError):
            User.objects.create_user(is_customer= False)
        with self.assertRaises(TypeError):
            User.objects.create_user(is_employee=True)

class CustomerTesCase(TestCase):  
    def setUp(self):
        self.user = User.objects.create(
            username = "monkey", email = "zaza@mail.com", is_customer = True
            )        
        self.customer = Customer.objects.last()

    def test_customer_attrs(self):
        self.assertTrue(hasattr(self.user,'customer'))   
        self.assertTrue(hasattr(self.customer,'user')) 
        self.assertEqual(self.customer.user.username, 'monkey') 

class EmployeeTesCase(TestCase):  
    def setUp(self):
        self.user = User.objects.create(
            username = "giraf", email = "foo@mail.com", is_employee = True
            )        
        self.employee = Employee.objects.last()

    def test_customer_attrs(self):
        self.assertTrue(hasattr(self.user,'employee'))   
        self.assertTrue(hasattr(self.employee,'user')) 
        self.assertEqual(self.employee.user.username, 'giraf') 
            
       
               

    
 
        
        