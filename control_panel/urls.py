from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('show_sector/<match_id>/<sector_slug>', views.show_sector, name='show_sector'),
    path('get_sector/', views.get_sector, name='get_sector'),
    path('save_sector/', views.save_sector, name='save_sector'),





]
