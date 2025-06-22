from django.core.management.base import BaseCommand
from core.models import Usuario
from django.contrib.auth import authenticate
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
            
            # Verificar que el usuario existente puede autenticarse
            user = authenticate(username=email, password=password)
            if user:
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Usuario existente puede autenticarse correctamente')
                )
            else:
                self.stdout.write(
                    self.style.ERROR(f'❌ Usuario existente pero no puede autenticarse. Actualizando contraseña...')
                )
                # Actualizar la contraseña del usuario existente
                user = Usuario.objects.get(email=email)
                user.set_password(password)
                user.is_staff = True
                user.is_superuser = True
                user.is_active = True
                user.email_verificado = True
                user.save()
                self.stdout.write(
                    self.style.SUCCESS(f'✅ Contraseña actualizada y permisos configurados')
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

            self.stdout.write('🔍 Verificando que el usuario se puede autenticar...')
            # Verificar que el usuario se puede autenticar
            auth_user = authenticate(username=email, password=password)
            if auth_user:
                self.stdout.write(
                    self.style.SUCCESS(
                        f'✅ Administrador creado y verificado exitosamente:\n'
                        f'   Email: {email}\n'
                        f'   Nombre: {nombre}\n'
                        f'   Contraseña: {password}\n'
                        f'   ID: {admin_user.id}\n'
                        f'   Autenticación: ✅ Funciona'
                    )
                )
            else:
                self.stdout.write(
                    self.style.ERROR(f'❌ Usuario creado pero no puede autenticarse')
                )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error al crear el administrador: {str(e)}')
            )
            # Mostrar más detalles del error
            import traceback
            self.stdout.write(self.style.ERROR(f'Traceback: {traceback.format_exc()}')) 