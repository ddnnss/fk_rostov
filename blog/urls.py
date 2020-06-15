from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', views.posts, name='posts'),
    path('<slug>', views.post, name='post'),



]
