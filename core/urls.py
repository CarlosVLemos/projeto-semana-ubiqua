from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from django.contrib import admin
from django.urls import path, include
from core import settings
from django.conf.urls.static import static


schema_view = get_schema_view(
   openapi.Info(
      title="API de Reciclagem",
      default_version='v1',
      description="Documentação automática da API",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('bi.urls')),
    path('', include('reciclagem.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
