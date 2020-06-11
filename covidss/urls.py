from django.contrib import admin
from django.urls import path, include
from assets import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('list_assets/', include('assets.urls')),
] 

#+ static(settings.MEDIA_URL, document_root=setting.MEDIA_ROOT)
