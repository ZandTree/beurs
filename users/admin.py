from django.contrib import admin
from .models import Employee, Customer
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import AdminPasswordChangeForm
from django.utils.translation import gettext as _
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm



User = get_user_model()

class UserAdmin(BaseUserAdmin):
    model = User
    search_fields = ('email','username','is_customer','is_employee','phone_number')
    form = UserChangeForm
    add_form = UserCreationForm 
    list_display = ( 'username','email','is_customer','is_employee','phone_number','last_login','is_superuser','is_staff','is_active',)
    list_filter = ('is_staff', 'is_active')
    
    #add key 'classes' with value [collapse ] to toggle Important Dates
    fieldsets = (
        (_('User'), {'fields': ('username','email', 'password','is_customer','is_employee','phone_number')}),
        (_('Permissions'), {'fields': ('is_superuser','is_staff','is_active','groups','user_permissions',)}),       
        (_('Important dates'), {'classes': ['collapse'],'fields': ('last_login','date_joined')}),
        
    )    
       
    # for changing a existed user <== UserCreationForm
    #otherwise it'll look for usename as ident
    add_fieldsets = (
        (('Add Your User'), {
            'classes': ('wide',),
            'fields': ('username','email', 'password1', 'password2'),
        }),
    )
    ordering = ('-date_joined',) #'email')
    # filter_vertical = ('groups','user_permissions')
    filter_horizontal = ('groups','user_permissions')# for the right widget
    


admin.site.register(User, UserAdmin)
admin.site.register(Customer)
admin.site.register(Employee)
