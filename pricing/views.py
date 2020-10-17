from django.shortcuts import render
from .models import Pricing,Photography,Photos,Processing,TypeOfCamera,Resolution,Term
from django.views.generic import ListView
# Create your views here.


class PricingList(ListView):
    model=Pricing


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["photography"] =Photography.objects.last() #query
        return context

    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["photos"] =Photos.objects.last() #query
        return context


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["processing"] =Processing.objects.last() #query
        return context


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["ceo"] =CEO.objects.last() #query
        return context



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["type_of_camera"] =TypeOfCamera.objects.last() #query
        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["resolution"] =Resolution.objects.last() #query
        return context

   