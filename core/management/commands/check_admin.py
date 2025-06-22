from django.core.management.base import BaseCommand
from core.models import Usuario
from django.contrib.auth import authenticate
import os

class Command(BaseCommand):
    help = 'Verifica que el administrador existe y puede autenticarse'

    def handle(self, *args, **options):
        email = os.environ.get('ADMIN_EMAIL', 'admin@admin.com')
        password = os.environ.get('ADMIN_PASSWORD', 'Admin0312')

        self.stdout.write(f'🔍 Verificando administrador...')
        self.stdout.write(f'   Email: {email}')

        # Verificar si el usuario existe
        try:
            user = Usuario.objects.get(email=email)
            self.stdout.write(f'✅ Usuario encontrado: {user.nombre}')
            self.stdout.write(f'   ID: {user.id}')
            self.stdout.write(f'   is_staff: {user.is_staff}')
            self.stdout.write(f'   is_superuser: {user.is_superuser}')
            self.stdout.write(f'   is_active: {user.is_active}')
            self.stdout.write(f'   email_verificado: {user.email_verificado}')
            
        except Usuario.DoesNotExist:
            self.stdout.write(
                self.style.ERROR(f'❌ Usuario con email {email} no existe')
            )
            return

        # Verificar autenticación
        auth_user = authenticate(username=email, password=password)
        if auth_user:
            self.stdout.write(
                self.style.SUCCESS(f'✅ Autenticación exitosa')
            )
            self.stdout.write(f'   Usuario autenticado: {auth_user.nombre}')
        else:
            self.stdout.write(
                self.style.ERROR(f'❌ Autenticación fallida')
            )
            
            # Intentar verificar la contraseña manualmente
            if user.check_password(password):
                self.stdout.write(f'✅ Contraseña es correcta')
            else:
                self.stdout.write(f'❌ Contraseña incorrecta') 