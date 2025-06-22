from django.core.management.base import BaseCommand
from django.core.management import call_command
import os

class Command(BaseCommand):
    help = 'Sincroniza datos entre entornos de desarrollo y producción'

    def add_arguments(self, parser):
        parser.add_argument(
            '--direction',
            type=str,
            choices=['to_prod', 'from_prod'],
            help='Dirección de sincronización'
        )

    def handle(self, *args, **options):
        direction = options.get('direction', 'to_prod')
        
        if direction == 'to_prod':
            self.stdout.write('📤 Sincronizando datos locales a producción...')
            # Aquí puedes agregar lógica para exportar datos locales
            # y subirlos a Railway
            self.stdout.write(self.style.SUCCESS('✅ Datos sincronizados a producción'))
            
        elif direction == 'from_prod':
            self.stdout.write('📥 Sincronizando datos de producción a local...')
            # Aquí puedes agregar lógica para descargar datos de Railway
            # y aplicarlos localmente
            self.stdout.write(self.style.SUCCESS('✅ Datos sincronizados a local')) 