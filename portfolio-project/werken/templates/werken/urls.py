from django.urls import path, include
from . import views

from django.conf import settings
import werken.views


urlpatterns = [
 path('admin/', admin.site.urls),
 #path('', views.home, name='home'),
 path('', werken.views.home, name='home'),
 path('werken/', include('werken.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
 
