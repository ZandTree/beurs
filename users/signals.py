from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Employee, Customer
from django.contrib.auth import get_user_model

User = get_user_model()


@receiver(post_save,sender = User)
def create_customer(sender,instance,created,**kwargs):
    """As New User and is_customer, create Customer"""
    if created and instance.is_customer:
        print("new customer created")
        Customer.objects.create(user=instance)
        instance.customer.save()


@receiver(post_save,sender = User)
def create_employee(sender,instance,created,**kwargs):
    """As New User created and is_employee|=> create Employee"""
    if created and instance.is_employee:
        print("new employee created")
        Employee.objects.create(user=instance)
        instance.employee.save()



