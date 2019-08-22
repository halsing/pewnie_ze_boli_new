from django.urls import path
from . import views

app_name = 'team'

urlpatterns = [
    path('', views.TeamList.as_view(), name='team_list')
]
