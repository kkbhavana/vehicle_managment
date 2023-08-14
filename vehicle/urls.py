from django.urls import path

from . import views
from .views import VechicleCreateView, VehicleListView, VehicleUpdateView, VehicleDeleteView, AdminCreateView, \
    AdminListView, AdminUpdateView, CustomerListView

urlpatterns = [
    path('home/',views.home,name='home'),
    path('vehicles_data_entry/',VechicleCreateView.as_view(),name='create'),
    path('vehicles_list/',VehicleListView.as_view(),name='list'),
    path('vehicles_update/<int:pk>/',VehicleUpdateView.as_view(),name='update'),
    path('vehicles_delete/<int:pk>/',VehicleDeleteView.as_view(),name='delete'),
    path('admin_vehicles_create/',AdminCreateView.as_view(),name='admin-create'),
    path('admin_vehicles_list/',AdminListView.as_view(),name='admin-list'),
    path('admin_update/<int:pk>/',AdminUpdateView.as_view(),name='admin-update'),
    path('customer_vehicles_list/',CustomerListView.as_view(),name='customer-list')

]




