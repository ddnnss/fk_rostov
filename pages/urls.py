from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.index, name='index'),
    path('offer/', views.offer, name='offer'),
    path('stadium/', views.stadium, name='stadium'),
    path('contact/', views.contact, name='contact'),
    path('matches/', views.matches, name='matches'),
    path('index.html', RedirectView.as_view(url='/', permanent=False), name='index1'),
    path('index.php', RedirectView.as_view(url='/', permanent=False), name='index2'),
    path('robots.txt', views.robots, name='robots'),


]
