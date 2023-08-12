from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .models import Vehicles


# Create your views here.
class VechicleCreateView(CreateView):
    model = Vehicles
    fields = '__all__'
    template_name = 'create_vehicle.html'
    success_url = reverse_lazy('list')

class VehicleListView(ListView):
    model = Vehicles
    context_object_name = 'vehicle'
    template_name = 'list_vechile.html'

class VehicleUpdateView(UpdateView):
    model = Vehicles
    fields = '__all__'
    template_name = 'create_vehicle.html'
    success_url = reverse_lazy('list')

class VehicleDeleteView(DeleteView):
    model = Vehicles
    template_name = 'delete_vehicle.html'
    success_url = reverse_lazy('list')





