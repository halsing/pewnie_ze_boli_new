from django.urls import path
from  . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.StudioGallery.as_view(), name='galleries'),
    path('guest_spot',views.GuestSpot.as_view(),name='guest_spot'),
    path('wall_of_fame', views.FameWall.as_view(), name='wall_of_fame'),
    path('<str:type>_studio/', views.studio_photos, name='gallery_studio'),
]

