from django.shortcuts import render
from .models import CEO,Team,Position
from django.views.generic import ListView

# Create your views here.

class TeamList(ListView):
    model=Team
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ceo"] = CEO.objects.last() #query
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posistion"] = Position.objects.last() #query
        return context





