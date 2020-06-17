from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [

    path('create_sectors', views.create_sectors, name='create_sectors'),
    path('get_sector_info', views.get_sector_info, name='get_sector_info'),


]
