from django.shortcuts import render
from .models import CEO,Team,Position
from django.views.generic import ListView

# Create your views here.

class CEOList(ListView):
    model=CEO


class TeamList(ListView):
    model=Team


class PositionList(ListView):
    model=Position