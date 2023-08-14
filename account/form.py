from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import SuperAdmin, Admin, Customer, User


class SuperAdminSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    register_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.register_number = self.cleaned_data.get('register_number')
        user.is_superadmin = True
        user.save()
        superadmin = SuperAdmin.objects.create(user=user)
        return user


class AdminSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    register_number = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.register_number = self.cleaned_data.get('register_number')
        user.is_admin = True
        user.save()
        admin = Admin.objects.create(user=user)
        return user


# customer

class CustomerSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.is_admin = True
        user.save()
        customer = Customer.objects.create(user=user)
        return user
