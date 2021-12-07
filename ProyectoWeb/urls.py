#urls del proyecto. se borró el import de las vistas y los url patterns fueron movidos a urls.py de la app.
from django.conf.urls import include
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),

    path('servicios/', include('servicios.urls')),

    path('blog/', include('blog.urls')),

    path('contacto/', include('contacto.urls')),

    path('tienda/', include('tienda.urls')),

    path('carro/', include('carro.urls')),
    
    path('', include('ProyectoWebApp.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)