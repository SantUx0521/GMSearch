from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

from .views import (
    RegistroUsuarioView, LoginView,
    GimnasioViewSet, RutinaViewSet, InventarioViewSet,
    MaquinaViewSet, FavoritoViewSet
)

router = DefaultRouter()
router.register(r'gimnasios', GimnasioViewSet)
router.register(r'rutinas', RutinaViewSet)
router.register(r'inventario', InventarioViewSet)
router.register(r'maquinas', MaquinaViewSet)
router.register(r'favoritos', FavoritoViewSet)

urlpatterns = [
    # Vistas HTML
    path('', views.index, name='index'),
    path('login-page/', views.login_page, name='login'),  # página de login HTML
    path('register-page/', views.register_page, name='register'),  # página de registro HTML
    path('register/', views.post_reg, name='post_reg'), #formulario que solicita datos adicionales al usuario

    # Endpoints API
    path('api/registro/', RegistroUsuarioView.as_view(), name='api_registro'),
    path('api/login/', LoginView.as_view(), name='api_login'),
    path('api/', include(router.urls)),
]
