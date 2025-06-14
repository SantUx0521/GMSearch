from django.db import migrations
from django.contrib.auth.hashers import make_password

def create_initial_data(apps, schema_editor):
    Usuario = apps.get_model('core', 'Usuario')
    Gimnasio = apps.get_model('core', 'Gimnasio')
    Maquina = apps.get_model('core', 'Maquina')
    Inventario = apps.get_model('core','Inventario')
    Rutina = apps.get_model('core','Rutina')

    usuario_dueño = Usuario.objects.create(
        email='dueño@ejemplo.com',
        nombre='Dueño Ejemplo',
        password=('password123'),
        direccion='Calle Principal 123',
        telefono='1234567890',
        es_dueño=True
    )

    gimnasio = Gimnasio.objects.create(
        dueño=usuario_dueño,
        nombre_gym='Gimnasio Prueba',
        ubicacion='Calle Falsa 123',
        calificacion=0,
        precio_inscripcion=50.00,
        descripcion='Un gimnasio de prueba',
        vistas=0
    )

    maquina = Maquina.objects.create(
        gimnasio=gimnasio,
        nombre='Máquina de Prensa',
        descripcion='Máquina para ejercicios de piernas'
    )

    producto = Inventario.objects.create(
        gimnasio=gimnasio,
        nombre_prod='Proteína Whey',
        descripcion='Suplemento proteico de alta calidad',
        precio=29.99
    )

    rutina = Rutina.objects.create(
        gimnasio=gimnasio,
        nombre='Rutina Básica',
        descripcion='Rutina para principiantes',
        duracion=45,
        nivel='Principiante'
    )

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_data),
    ]
