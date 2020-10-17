from django.urls import path
from .views import PortraitList


app_name='gallery'

urlpatterns=[
    path('',PortraitList.as_view(),name='portrait_list')
]