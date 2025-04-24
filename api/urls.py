from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import UnidadeViewSet, CursoViewSet, TurmaViewSet, AlunoViewSet, TipoResiduosViewSet, ReciclagemViewSet, UserLoginView, UserTokenRefreshView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from core.swagger import CustomSchemaGenerator

router = DefaultRouter()
router.register(r'unidades', UnidadeViewSet)
router.register(r'cursos', CursoViewSet)
router.register(r'turmas', TurmaViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'tipos-residuos', TipoResiduosViewSet)
router.register(r'reciclagem', ReciclagemViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="API de Reciclagem",
      default_version='v1',
      description="Documentação automática da API",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
   generator_class=CustomSchemaGenerator,
)

urlpatterns = [
    path('api/login/', UserLoginView.as_view(), name='login'),
    path('api/token/refresh/', UserTokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls)),
    path('api/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]