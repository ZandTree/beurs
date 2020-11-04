from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee, Customer
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save,sender = Customer)
def create_customer(sender,instance,created,**kwargs):
    """As New Customer created make user is_customer True"""
    if created and not instance.user.is_customer:
        print("new customer created")
        instance.user.is_customer = True
        instance.user.save()

@receiver(post_save,sender = Employee)
def create_employee(sender,instance,created,**kwargs):
    """As New Customer created make user is_customer True"""
   
    if created and not instance.user.is_employee:
        print("new employee created")
        instance.user.is_emloyee = True
        instance.user.save()


