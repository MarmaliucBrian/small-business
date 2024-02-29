from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from users.forms import UserForm
from users.models import UserModel


# Create your views here.


class UsersCreateView(CreateView):
    model = UserModel
    form_class = UserForm
    template_name = 'create_update_form.html'
    success_url = reverse_lazy('users-all')

class UsersListView(ListView):
    model = UserModel
    template_name = 'users/all.html'


class UsersUpdateView(UpdateView):
    model = UserModel
    form_class = UserForm
    template_name = 'create_update_form.html'
    success_url = reverse_lazy('users-all')

class UsersDeleteView(DeleteView):
    model = UserModel
    form_class = UserForm
    template_name = 'delete_form.html'
    success_url = reverse_lazy('users-all')

class UsersDetailView(DetailView):
    model = UserModel
    template_name = 'users/detalii.html'