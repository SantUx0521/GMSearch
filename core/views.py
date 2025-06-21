import json
from django.http import JsonResponse
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
from django.contrib.auth import login
#verificacion de email
from django.utils import timezone
from django.core.mail import send_mail
from django.conf import settings
import secrets
from datetime import timedelta
from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth import logout

def index(request):
    return render(request, 'core/index.html')
# ----------------------------
# buscar un gimnasio por nombre
# ----------------------------
def buscar_gimnasios(request):  # <--- Aquí la nueva view
    query = request.GET.get('q', '')
    resultados = []
    if query:
        resultados = Gimnasio.objects.filter(nombre_gym__icontains=query)
    return render(request, 'core/search.html', {'query': query, 'resultados': resultados})

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

@ensure_csrf_cookie
def register_page(request):
    if request.method == 'POST':
        tipo = request.POST.get('tipo_usuario')
        nombre = request.POST['nombre']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST.get('confirm_password')
        
        # Validar que las contraseñas coincidan
        if password != confirm_password:
            return render(request, 'core/register.html', {'error': 'Las contraseñas no coinciden'})
        
        # Validar que el correo no esté registrado
        if Usuario.objects.filter(email=email).exists():
            return render(request, 'core/register.html', {'error': 'Este correo electrónico ya está registrado'})
        
        # Generar token de verificación
        token = secrets.token_urlsafe(32)
        fecha_expiracion = timezone.now() + timedelta(hours=24)
        
        usuario = Usuario.objects.create(
            nombre=nombre,
            email=email,
            password=make_password(password),
            token_verificacion=token,
            fecha_token=fecha_expiracion,
            es_dueño=(tipo == 'dueño')
        )
        
        # Enviar email de verificación
        send_mail(
            'Verifica tu cuenta en GMSearch',
            f'Por favor, verifica tu cuenta haciendo clic en el siguiente enlace:\n\n'
            f'http://{request.get_host()}/verificar-email/{token}/\n\n'
            f'Este enlace expirará en 24 horas.',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        
        return render(request, 'core/verificacion_pendiente.html')
    if 'register-own' in request.path: #en caso de que el registro venga por parte de un dueño de gimnasio toma los datos del html correspondiente
        return render(request, 'core/registerOwn.html')
    return render(request, 'core/register.html')

def verificar_email(request, token):
    try:
        usuario = Usuario.objects.get(token_verificacion=token)
        if usuario.fecha_token and usuario.fecha_token > timezone.now():
            usuario.email_verificado = True
            usuario.is_active = True
            usuario.token_verificacion = None
            usuario.fecha_token = None
            usuario.save()
            
            # Guardar datos en la sesión
            request.session['nombre_usuario'] = usuario.nombre
            request.session['email_usuario'] = usuario.email
            
            login(request, usuario)
            if usuario.es_dueño:  
                return redirect('reg_gym')  
            else:
                return redirect('post_reg')
        else:
            return render(request, 'core/token_expirado.html')
    except Usuario.DoesNotExist:
        return render(request, 'core/token_invalido.html')

def normalizar_estatura(estatura_str):
    if not estatura_str:
        return None
    
    # Eliminar espacios y convertir a minúsculas
    estatura_str = estatura_str.strip().lower()
    
    # Si ya está en centímetros (número sin punto ni coma)
    if estatura_str.isdigit():
        return float(estatura_str)
    
    # Reemplazar coma por punto para estandarizar
    estatura_str = estatura_str.replace(',', '.')
    
    try:
        # Convertir a float
        estatura = float(estatura_str)
        
        # Si el número es menor a 3, asumimos que está en metros
        if estatura < 3:
            return estatura * 100  # Convertir a centímetros
        else:
            return estatura  # Ya está en centímetros
    except ValueError:
        return None

def post_reg(request):
    if request.method == 'POST': # utilizado para añadir datos adicionales sobre el usuario, que se veran desplegados en su profile
        usuario = request.user
        usuario.nombres = request.POST.get('nombres')
        usuario.apellidos = request.POST.get('apellidos')
        usuario.edad = request.POST.get('edad') or None
        usuario.telefono = request.POST.get('telefono')
        
        # Normalizar la estatura
        estatura = request.POST.get('estatura')
        usuario.estatura = normalizar_estatura(estatura)
        
        usuario.peso = request.POST.get('peso') or None
        usuario.sexo = request.POST.get('sexo')
        usuario.save()
        return redirect('profile')
    
    # Obtener datos de la sesión
    context = {
        'nombre_usuario': request.session.get('nombre_usuario', ''),
        'email_usuario': request.session.get('email_usuario', '')
    }
    return render(request, 'core/PostRegister.html', context)

def profile(request):
    usuario = request.user  # necesario para acceder directamente al usuario
    return render(request, 'core/profile.html', {'usuario': usuario})

def edit_profile(request):
    usuario = request.user
    
    if request.method == 'POST':
        print("DEBUG: Método POST recibido")
        print("DEBUG: FILES disponibles:", request.FILES.keys())
        
        # Actualizar los datos del usuario
        usuario.nombre = request.POST.get('nombre', usuario.nombre)
        usuario.email = request.POST.get('email', usuario.email)
        usuario.edad = request.POST.get('edad') or None
        usuario.telefono = request.POST.get('telefono', usuario.telefono)
        
        # Normalizar la estatura
        estatura = request.POST.get('estatura')
        usuario.estatura = normalizar_estatura(estatura)
        
        usuario.peso = request.POST.get('peso') or None
        usuario.sexo = request.POST.get('sexo', usuario.sexo)
        
        # Manejar la subida de la foto de perfil
        if 'foto_perfil' in request.FILES:
            print("DEBUG: Foto de perfil encontrada en FILES")
            usuario.foto_perfil = request.FILES['foto_perfil']
            print("DEBUG: Foto asignada:", usuario.foto_perfil)
        else:
            print("DEBUG: No se encontró foto_perfil en FILES")
        
        # Guardar los cambios
        usuario.save()
        print("DEBUG: Usuario guardado. Foto actual:", usuario.foto_perfil)
        
        return redirect('profile')
    
    return render(request, 'core/edit_profile.html', {'usuario': usuario})
    
def login_usuario(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')
        usuario = authenticate(request, username=email, password=password)

        if usuario is not None:
            login(request, usuario)
            return JsonResponse({'mensaje': 'Inicio de sesión exitoso'})
        else:
            return JsonResponse({'error': 'correo y/o contraseña incorrecta'}, status=400)
        
def search(request):
    gimnasios = Gimnasio.objects.all()  
    return render(request, 'core/search.html', {'gimnasios': gimnasios})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
    return redirect('index')

def register_gym(request):
    if request.method == 'POST':
        nombre_gym = request.POST['nombre_gym']
        ubicacion = request.POST['ubicacion']
        precio = request.POST['precio_inscripcion']
        descripcion = request.POST['descripcion']
        imagen = request.FILES.get('imagen')

        gimnasio = Gimnasio.objects.create(
            dueño=request.user,
            nombre_gym=nombre_gym,
            ubicacion=ubicacion,
            precio_inscripcion=precio,
            descripcion=descripcion,
            imagen=imagen
        )
        return redirect('post_register_gym', gimnasio_id=gimnasio.codigo_gym)

    return render(request, 'core/registerGym.html')

def post_register_gym(request, gimnasio_id):
    gimnasio = Gimnasio.objects.get(pk=gimnasio_id)

    if request.method == 'POST':
        # Datos para las maquinas
        nombre_maquina = request.POST.get('nombre_maquina')
        descripcion_maquina = request.POST.get('descripcion_maquina')

        if nombre_maquina and descripcion_maquina:
            Maquina.objects.create(
                gimnasio=gimnasio,
                nombre=nombre_maquina,
                descripcion=descripcion_maquina
            )

        # Datos para los productos
        nombre_prod = request.POST.get('nombre_prod')
        descripcion_prod = request.POST.get('descripcion_prod')
        precio_prod = request.POST.get('precio_prod')

        if nombre_prod and descripcion_prod and precio_prod:
            Inventario.objects.create(
                gimnasio=gimnasio,
                nombre_prod=nombre_prod,
                descripcion=descripcion_prod,
                precio=precio_prod
            )

    return render(request, 'core/gymData.html', {'gimnasio': gimnasio})