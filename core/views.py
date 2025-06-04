from django.shortcuts import redirect, render
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import GimnasioFilter

def index(request):
    return render(request, 'core/index.html') #Esto es necesario para seguir con la arquitectura cliente-servidor.

# ----------------------------
# Registro de usuario
# ----------------------------
class RegistroUsuarioView(generics.CreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.AllowAny]


# ----------------------------
# Login (Token)
# ----------------------------
class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        usuario = authenticate(request, email=email, password=password)
        if usuario:
            token, created = Token.objects.get_or_create(user=usuario)
            return Response({'token': token.key})
        return Response({'error': 'Credenciales inválidas'}, status=400)


# ----------------------------
# Gimnasio
# ----------------------------

class GimnasioViewSet(viewsets.ModelViewSet):
    queryset = Gimnasio.objects.all()
    serializer_class = GimnasioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GimnasioFilter


# ----------------------------
# Rutinas
# ----------------------------
class RutinaViewSet(viewsets.ModelViewSet):
    queryset = Rutina.objects.all()
    serializer_class = RutinaSerializer


# ----------------------------
# Inventario
# ----------------------------
class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer


# ----------------------------
# Maquinas
# ----------------------------
class MaquinaViewSet(viewsets.ModelViewSet):
    queryset = Maquina.objects.all()
    serializer_class = MaquinaSerializer


# ----------------------------
# Favoritos
# ----------------------------
class FavoritoViewSet(viewsets.ModelViewSet):
    queryset = Favorito.objects.all()
    serializer_class = FavoritoSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = Favorito.objects.filter(usuario=user)
        gimnasio_qs = queryset.values_list('gimnasio', flat=True)

        # Aplicar filtros adicionales si es necesario
        ubicacion = self.request.query_params.get('ubicacion')
        precio_max = self.request.query_params.get('precio_max')
        calificacion = self.request.query_params.get('calificacion')

        if ubicacion:
            gimnasio_qs = gimnasio_qs.filter(ubicacion__icontains=ubicacion)
        if precio_max:
            gimnasio_qs = gimnasio_qs.filter(precio_inscripcion__lte=precio_max)
        if calificacion:
            gimnasio_qs = gimnasio_qs.filter(calificacion__gte=calificacion)

        return queryset.filter(gimnasio__in=gimnasio_qs)

#----------------------------
# Login (HTML)
# ---------------------------    
def login_page(request):
    return render(request, 'core/login.html')

def register_page(request):
    return render(request, 'core/register.html')

def post_reg(request):
    return render(request, 'core/PostRegister.html') 

def profile(request):
    return render(request, 'core/profile.html')