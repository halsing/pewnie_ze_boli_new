from django.urls import path

from . import views
from team import views as team_views

app_name = 'base'

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('contact/', views.contact, name="contact"),
    path('faq/', views.faq, name="faq"),
    path('laser/', views.Laser.as_view(), name='laser'),
    path('<slug:artist>/',
         team_views.ArtistProfile.as_view(), name='artist_profile')
]
