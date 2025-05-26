from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegistroUsuarioView, LoginView,
    GimnasioViewSet, RutinaViewSet, InventarioViewSet,
    MaquinaViewSet, FavoritoViewSet
)
#urlpatterns = [
 #   path('', views.index, name='index'),
#]


router = DefaultRouter()
router.register(r'gimnasios', GimnasioViewSet)
router.register(r'rutinas', RutinaViewSet)
router.register(r'inventario', InventarioViewSet)
router.register(r'maquinas', MaquinaViewSet)
router.register(r'favoritos', FavoritoViewSet)

urlpatterns = [
    path('registro/', RegistroUsuarioView.as_view(), name='registro'),
    path('login/', LoginView.as_view(), name='login'),
    path('', include(router.urls)),
]
