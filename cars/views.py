from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .models import Vehicles

# Create your views here.
class VehicleListView(ListView):
    model = Vehicles
    query_pk_and_slug = True