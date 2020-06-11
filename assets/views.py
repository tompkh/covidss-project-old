from django.shortcuts import render
from .models import Asset

def home(request):
    assets = Asset.objects
    return render(request, 'assets/home.html', {'assets':assets})

def list_assets(request):
    return render(request, 'assets/list_assets.html' )