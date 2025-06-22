from django.core.management.base import BaseCommand
from core.models import Usuario
import os

class Command(BaseCommand):
    help = 'Crea un usuario administrador usando variables de entorno'

    def handle(self, *args, **options):
        # Obtener valores de las variables de entorno
        email = os.environ.get('ADMIN_EMAIL', 'admin@admin.com')
        nombre = os.environ.get('ADMIN_NAME', 'Administrador')
        password = os.environ.get('ADMIN_PASSWORD', 'Admin0312')

        self.stdout.write(f'🔧 Configurando administrador desde variables de entorno...')
        self.stdout.write(f'   Email: {email}')
        self.stdout.write(f'   Nombre: {nombre}')
        self.stdout.write(f'   Password: {"*" * len(password)}')

        # Verificar si el usuario ya existe
        if Usuario.objects.filter(email=email).exists():
            self.stdout.write(
                self.style.WARNING(f'⚠️ El usuario con email {email} ya existe.')
            )
            return

        # Crear el usuario administrador
        try:
            self.stdout.write('📝 Creando usuario...')
            admin_user = Usuario.objects.create_user(
                email=email,
                nombre=nombre,
                password=password
            )
            
            self.stdout.write('🔐 Configurando permisos de administrador...')
            # Configurar como administrador
            admin_user.is_staff = True
            admin_user.is_superuser = True
            admin_user.is_active = True
            admin_user.email_verificado = True
            admin_user.save()

            self.stdout.write(
                self.style.SUCCESS(
                    f'✅ Administrador creado exitosamente:\n'
                    f'   Email: {email}\n'
                    f'   Nombre: {nombre}\n'
                    f'   Contraseña: {password}\n'
                    f'   ID: {admin_user.id}'
                )
            )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error al crear el administrador: {str(e)}')
            )
            # Mostrar más detalles del error
            import traceback
            self.stdout.write(self.style.ERROR(f'Traceback: {traceback.format_exc()}')) 