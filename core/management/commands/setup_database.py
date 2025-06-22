from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db import connection
import os

class Command(BaseCommand):
    help = 'Configura la base de datos inicial'

    def handle(self, *args, **options):
        self.stdout.write('🗄️ Configurando base de datos...')
        
        # Verificar conexión a la base de datos
        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT 1")
            self.stdout.write('✅ Conexión a base de datos exitosa')
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error de conexión: {str(e)}')
            )
            return

        # Aplicar migraciones
        self.stdout.write('📋 Aplicando migraciones...')
        try:
            call_command('migrate', verbosity=0)
            self.stdout.write('✅ Migraciones aplicadas')
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error en migraciones: {str(e)}')
            )
            return

        # Crear administrador
        self.stdout.write('👤 Creando administrador...')
        try:
            call_command('setup_admin', verbosity=0)
            self.stdout.write('✅ Administrador configurado')
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error creando administrador: {str(e)}')
            )

        # Verificar configuración
        self.stdout.write('🔍 Verificando configuración...')
        try:
            call_command('check_admin', verbosity=0)
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(f'❌ Error en verificación: {str(e)}')
            )

        self.stdout.write(
            self.style.SUCCESS('🎉 Base de datos configurada exitosamente')
        ) 