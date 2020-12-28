from django.urls import path
from .views import (CustomerRegister,
                    CustomerDashboard,
                    EmployeeRegister,
                    EmployeeDashboard,
                    logout
                    )

app_name = 'users'

urlpatterns = [
    path('customer-registration/', CustomerRegister.as_view(),name='customer-signup'),
    path('customer-dashboard/', CustomerDashboard.as_view(),name='customer-dashboard'),
    path('employee-registration/', EmployeeRegister.as_view(),name='employee-signup'),
    path('employee-dashboard/', EmployeeDashboard.as_view(),name='employee-dashboard'),
    path('logout/',logout,name='logout')
    
]