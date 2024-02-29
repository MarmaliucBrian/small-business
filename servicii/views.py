from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, UpdateView, DeleteView, CreateView

from servicii.forms import ServiciiForm
from servicii.models import ServiciiModels







class ServiciiDetailView(DetailView):
    template_name = "servicii/detalii.html"
    model = ServiciiModels

class ServiciiListView(ListView):
    template_name = "servicii/all.html"
    model = ServiciiModels


class ServiciiUpdateView(UpdateView):
    form_class = ServiciiForm
    template_name = "create_update_form.html"
    model = ServiciiModels
    success_url = reverse_lazy('serviciu-all')

class ServiciiDeleteView(DeleteView):
    template_name = "delete_form.html"
    model = ServiciiModels
    success_msg =  "Ati sters serviciul"
    success_url = reverse_lazy('serviciu-all')

class ServiciiCreateView(CreateView):
    form_class = ServiciiForm
    template_name = "create_update_form.html"
    model = ServiciiModels
    success_url = reverse_lazy('serviciu-all')
