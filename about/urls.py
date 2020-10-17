from django.urls import path
from .views import CEOList,TeamList,PositionList

app_name='about'

urlpatterns=[
    path('',CEOList.as_view(),name='ceo_list'),
    path('',TeamList.as_view(),name='team_list'),
    path('',PositionList.as_view(),name='position_list')
]