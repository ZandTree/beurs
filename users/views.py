from django.views.generic import CreateView
from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib.auth.forms import UserCreationForm
from .forms import *

class CustReg(CreateView):
    model = User
    form_class= CustomerCreationForm
    template_name = 'users/cust_registration.html'
    success_url = '/'
   