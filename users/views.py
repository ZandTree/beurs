from django.contrib.auth.decorators import login_required,permission_required
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin as LRM
from django.shortcuts import redirect
from django.contrib.auth import logout as django_logout
from django.conf import  settings
from django.http import JsonResponse
from .forms import *


# User = get_user_model()


class CustomerRegister(LRM, CreateView):
    form_class = CustomerForm
    success_url = 'customer/customer-dashboard.html'
    template_name = 'customer/customer-form.html'

    def form_valid(self, form):
        """ if for valid, obj customer wiil be created
        and user attr is_customer => True"""
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        self.request.user.is_customer = True
        self.request.user.save()
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {"msg": "Submission successful"}
            print("success url", self.success_url)
            return JsonResponse({"redirect_to": self.success_url})
        else:
            return response

    def form_invalid(self, form):
        """ If form is invalid return status 400 array of errors """
        response = super().form_invalid(form)
        msg = "something went wrong"
        errors = form.errors.as_json()  # string
        return JsonResponse({"msg": msg, "errors": errors}, status=400)


class CustomerDashboard(LRM, TemplateView):
    template_name = 'customer/customer-dashboard.html'


class EmployeeRegister(LRM, CreateView):
    """ if for valid, obj employee wiil be created
    and user attr is_employee => True"""
    form_class = EmployeeForm
    success_url = 'employee/employee-dashboard.html'
    template_name = 'employee/employee-form.html'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        self.request.user.is_employee = True
        self.request.user.save()
        response = super().form_valid(form)
        if self.request.is_ajax():
            data = {"msg": "Submission successful"}
            return JsonResponse({"data": data})
        else:
            return response

    def form_invalid(self, form):
        """ If form is invalid return status 400 array of errors """
        response = super().form_invalid(form)
        msg = "something went wrong"
        errors = form.errors.as_json()  # string
        return JsonResponse({"msg": msg, "errors": errors}, status=400)


class EmployeeDashboard(LRM, TemplateView):
    template_name = 'employee/employee-dashboard.html'

@login_required
def logout(request):
    django_logout(request)
    domain = settings.SOCIAL_AUTH_AUTH0_DOMAIN
    client_id = settings.SOCIAL_AUTH_AUTH0_KEY
    return_to = "http://127.0.0.1:8000"
    return redirect(f"https://{domain}/v2/logout?client_id={client_id}&returnTo={return_to}")