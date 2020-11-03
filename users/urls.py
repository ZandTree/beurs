from django.urls import path
from .views import CustReg

app_name = 'users'

urlpatterns = [
    path('',CustReg.as_view(),name="customer-signup")
]