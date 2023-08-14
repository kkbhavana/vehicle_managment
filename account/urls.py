from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import SuperAdminSignupView, SuperAdminLoginView, AdminSignupView, AdminLoginView, CustomerSignupView, \
    CustomerLoginView

urlpatterns = [
    path('super_admin_signup/', SuperAdminSignupView.as_view(), name='super_signup'),
    path('super_login/', SuperAdminLoginView.as_view(), name='super_login'),
    path('admin_signup/', AdminSignupView.as_view(), name='admin_signup'),
    path('admin_login/', AdminLoginView.as_view(), name='admin_login'),
    path('customer_signup/', CustomerSignupView.as_view(), name='customer_signup'),
    path('customer_login/', CustomerLoginView.as_view(), name='customer_login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
