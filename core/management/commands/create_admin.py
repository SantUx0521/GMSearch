from django.core.management.base import BaseCommand
from core.models import Usuario

class Command(BaseCommand):
    help = 'Crea un usuario administrador'

    def add_arguments(self, parser):
        parser.add_argument('--email', type=str, required=True, help='Email del administrador')
        parser.add_argument('--nombre', type=str, required=True, help='Nombre del administrador')
        parser.add_argument('--password', type=str, required=True, help='Contraseña del administrador')

    def handle(self, *args, **options):
        email = options['email']
        nombre = options['nombre']
        password = options['password']

        # Verificar si el usuario ya existe
        if Usuario.objects.filter(email=email).exists():
            self.stdout.write(
                self.style.WARNING(f'El usuario con email {email} ya existe.')
            )
            return

        # Crear el usuario administrador
        try:
            admin_user = Usuario.objects.create_user(
                email=email,
                nombre=nombre,
                password=password
            )
            
            # Configurar como administrador
            admin_user.is_staff = True
            admin_user.is_superuser = True
            admin_user.is_active = True
            admin_user.email_verificado = True
            admin_user.save()

            self.stdout.write(
                self.style.SUCCESS(
                    f'Administrador creado exitosamente:\n'
                    f'Email: {email}\n'
                    f'Nombre: {nombre}\n'
                    f'Contraseña: {password}'
                )
            )
            
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'Error al crear el administrador: {str(e)}')
            ) 