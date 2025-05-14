from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from dashboard.views import dashboard_view


urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include('accounts.urls')),
    path('dashboard/', login_required(dashboard_view), name='dashboard'), 
    path('krishok/', include('krishok_profile.urls')),
    path('crops/', include('crop_management.urls')),
    path('weather/', include('weather.urls')),
    path('disease/', include('disease_detection.urls')),
    path('fertilizers/', include('fertilizer_management.urls')),
    path('products/', include('marketing.urls')),
    path('govt/', include('govt_assistance.urls')),
    path('advice/', include('advisory_forum.urls')),
    

    



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
