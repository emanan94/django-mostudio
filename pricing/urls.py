from django.urls import path
from .views import PricingList


app_name='pricing'


urlpatterns=[
    path('',PricingList.as_view(),name='pricing')
]