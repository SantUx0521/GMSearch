from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from django.conf import settings
from django.conf.urls.static import static

from .views import (
    RegistroUsuarioView, LoginView,
    GimnasioViewSet, RutinaViewSet, InventarioViewSet,
    MaquinaViewSet, FavoritoViewSet,ReseñaViewSet
)

router = DefaultRouter()
router.register(r'gimnasios', GimnasioViewSet)
router.register(r'rutinas', RutinaViewSet)
router.register(r'inventario', InventarioViewSet)
router.register(r'maquinas', MaquinaViewSet)
router.register(r'favoritos', FavoritoViewSet)
router.register(r'resenas', ReseñaViewSet)

urlpatterns = [
    # Vistas HTML
    path('', views.index, name='index'),
    path('login-page/', views.login_page, name='login'),  # página de login HTML
    path('register-page/', views.register_page, name='register'),  # página de registro HTML
    path('register-own/', views.register_page, name='register_own'),
    path('register/', views.post_reg, name='post_reg'), #formulario que solicita datos adicionales al usuario
    path('profile', views.profile, name= "profile"),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('login-usuario/', views.login_usuario, name='login_usuario'),
    path('verificar-email/<str:token>/', views.verificar_email, name='verificar_email'),
    path('search/', views.search, name= 'search'),
    path('logout/', views.logout_view, name='logout'),
    path('register-gym/', views.register_gym, name='reg_gym'),
    path('Details_gym/<int:gimnasio_id>/', views.post_register_gym, name='post_register_gym'),
    path('buscar/', views.buscar_gimnasios, name='buscar_gimnasios'),
    path('api/gimnasio/<int:gimnasio_id>/detalle/', views.gimnasio_detalle_api, name='gimnasio_detalle_api'),

    # Endpoints API
    path('api/', include(router.urls)),
    path('api/registro/', RegistroUsuarioView.as_view(), name='api_registro'),
    path('api/login/', LoginView.as_view(), name='api_login'),
    path('api/', include(router.urls)),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
