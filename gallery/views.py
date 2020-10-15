from django.shortcuts import render
from .models import Portrait
from django.views.generic import ListView

# Create your views here.

class PortraitList(ListView):
    model=Portrait