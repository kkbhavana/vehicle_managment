from django.urls import path

from .views import VechicleCreateView, VehicleListView, VehicleUpdateView, VehicleDeleteView

urlpatterns = [
    path('vehicles_data_entry/',VechicleCreateView.as_view(),name='create'),
    path('vehicles_list/',VehicleListView.as_view(),name='list'),
    path('vehicles_update/<int:pk>/',VehicleUpdateView.as_view(),name='update'),
    path('vehicles_delete/<int:pk>/',VehicleDeleteView.as_view(),name='delete'),


]
