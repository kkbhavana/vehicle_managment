from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .form import SuperAdminSignUpForm, AdminSignUpForm, CustomerSignUpForm
from .models import User, SuperAdmin


# Create your views here.
# superadmin
class SuperAdminSignupView(CreateView):
    model = User
    form_class = SuperAdminSignUpForm
    template_name = 'signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'superadmin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('list')


class SuperAdminLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('list')


# admin
class AdminSignupView(CreateView):
    model = User
    form_class = AdminSignUpForm
    template_name = 'admin_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'admin'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('admin-list')


class AdminLoginView(LoginView):
    template_name = 'admin_login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('admin-list')


# customer

class CustomerSignupView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'customer_signup.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('customer-list')


class CustomerLoginView(LoginView):
    template_name = 'customer_login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('customer-list')
