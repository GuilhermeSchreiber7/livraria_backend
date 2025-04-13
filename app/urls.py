from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from django.conf import settings
from django.conf.urls.static import static
import uploader
from uploader.router import router as uploader_router

from rest_framework.routers import DefaultRouter

from core.views import UserViewSet, AutorViewSet, EditoraViewSet, CategoriaViewSet, LivroViewSet
router = DefaultRouter()

router.register(r"livros", LivroViewSet)
router.register(r"autores", AutorViewSet)
router.register(r"editoras", EditoraViewSet)
router.register(r"categorias", CategoriaViewSet)
router.register(r'usuarios', UserViewSet, basename='usuarios')

urlpatterns = [
    path('admin/', admin.site.urls),
    # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path(
        'api/swagger/',
        SpectacularSwaggerView.as_view(url_name='schema'),
        name='swagger-ui',
    ),
    path(
        'api/redoc/',
        SpectacularRedocView.as_view(url_name='schema'),
        name='redoc',
    ),
    # API
    path('api/', include(router.urls)),
]
