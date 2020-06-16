from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [

    path('s_417', views.s_417, name='s_417'),


]
