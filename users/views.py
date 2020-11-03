from django.views.generic import CreateView,RedirectView
from django.contrib.auth import get_user_model

User = get_user_model()

from django.contrib.auth.forms import UserCreationForm
from .forms import *

class CustReg(RedirectView):
    pattern_name = 'users:customer-dashboard'
    
    def get_redirect_url(self):
        # some logic here
        # user gets is_customer True
        return super().get_redirect_url(*args,**kwargs) 


   