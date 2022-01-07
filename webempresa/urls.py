from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from services import views as services_views

urlpatterns = [
    # Path core
    path('', include('core.urls')), 
    # Paths Services
    path('services/', include('services.urls')), 
    # Path Blog
    path('blog/', include('blog.urls')), 
    # Path Pages
    path('page/', include('pages.urls')), 
    # Path Contact
    path('contact/', include('contact.urls')), 
    # Path Admin
    path('admin/', admin.site.urls),
    
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
