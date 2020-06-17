from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [

    path('<match_slug>', views.show_stadium, name='show_stadium'),


]
