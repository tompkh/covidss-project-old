from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_assets, name='list_assets'),
] 