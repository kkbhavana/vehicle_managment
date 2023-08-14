from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from .models import Vehicles


# Create your views here.
def home(request):
    return render(request, 'home.html')


# superadmin
class VechicleCreateView(LoginRequiredMixin, CreateView):
    model = Vehicles
    fields = '__all__'
    template_name = 'create_vehicle.html'
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(VechicleCreateView, self).form_valid(form)


class VehicleListView(LoginRequiredMixin, ListView):
    model = Vehicles
    context_object_name = 'vehicle'
    template_name = 'list_vechile.html'


class VehicleUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicles
    fields = '__all__'
    template_name = 'create_vehicle.html'
    success_url = reverse_lazy('list')


class VehicleDeleteView(LoginRequiredMixin, DeleteView):
    model = Vehicles
    template_name = 'delete_vehicle.html'
    success_url = reverse_lazy('list')


# admin
class AdminCreateView(LoginRequiredMixin, CreateView):
    model = Vehicles
    fields = '__all__'
    template_name = 'admin_create.html'
    success_url = reverse_lazy('admin_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(AdminCreateView, self).form_valid(form)


class AdminListView(LoginRequiredMixin, ListView):
    model = Vehicles
    context_object_name = 'vehicle'
    template_name = 'admin_list.html'


class AdminUpdateView(LoginRequiredMixin, UpdateView):
    model = Vehicles
    fields = '__all__'
    template_name = 'admin_create.html'
    success_url = reverse_lazy('admin-list')


# customer
class CustomerListView(LoginRequiredMixin, ListView):
    model = Vehicles
    context_object_name = 'vehicle'
    template_name = 'customer_list.html'
