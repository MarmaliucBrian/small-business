
from django.shortcuts import render
from django.views.generic import ListView  # Correct import for ListView
from servicii.models import ServiciiModels

def home(request):
    return render(request, 'home/home.html', context={})

class HomeView(ListView):
    template_name = 'home/home.html'
    model = ServiciiModels