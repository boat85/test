from django.urls import path
from . import views

urlpatterns = [
  path('', views.showdata),
  path('showdatafs', views.showdatafs)
]