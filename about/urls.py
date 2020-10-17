from django.urls import path

from .views import TeamList


app_name='about'

urlpatterns=[
    path('',TeamList.as_view(),name='team_list')

]