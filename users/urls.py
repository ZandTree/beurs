from django.urls import path
from .views import (CustomerRegister,
                    CustomerDashboard,
                    EmployeeRegister,
                    EmployeeDashboard
                    )

app_name = 'users'

urlpatterns = [
    path('customer-registation', CustomerRegister.as_view(),name='customer-signup'),   
    path('customer-dashboard', CustomerDashboard.as_view(),name='customer-dashboard'),  
    path('employee-registation', EmployeeRegister.as_view(),name='employee-signup'),   
    path('employee-dashboard', EmployeeDashboard.as_view(),name='employee-dashboard'),  
    
]