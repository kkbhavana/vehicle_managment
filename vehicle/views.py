from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .models import Vehicles



# Create your views here.

def home(request):
    return render(request,'home.html')
#superadmin
class VechicleCreateView(CreateView):
    model = Vehicles
    fields = '__all__'
    template_name = 'create_vehicle.html'
    success_url = reverse_lazy('list')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(VechicleCreateView,self).form_valid(form)

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


#admin
class AdminCreateView(CreateView):
    model = Vehicles
    fields = '__all__'
    template_name = 'admin_create.html'
    success_url = reverse_lazy('admin_list')


    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AdminCreateView,self).form_valid(form)

class AdminListView(ListView):
    model = Vehicles
    context_object_name = 'vehicle'
    template_name = 'admin_list.html'


class AdminUpdateView(UpdateView):
    model = Vehicles
    fields = '__all__'
    template_name = 'admin_create.html'
    success_url = reverse_lazy('admin-list')


#customer
class CustomerListView(ListView):
    model = Vehicles
    context_object_name = 'vehicle'
    template_name = 'customer_list.html'