from django.db import models

class FichaBiometrica(models.Model):
    ficha_usuario = models.AutoField(primary_key=True)
    altura = models.DecimalField(max_digits=5, decimal_places=2)
    peso = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"Ficha {self.ficha_usuario}"

class Usuario(models.Model):
    username = None  # Eliminamos el campo username original
    email = models.EmailField(unique=True)
    
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=20)
    es_dueño = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    def __str__(self):
        return self.email

    def __str__(self):
        return self.nombre

class Gimnasio(models.Model):
    codigo_gym = models.AutoField(primary_key=True)
    dueño = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='gimnasios')
    nombre_gym = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255)
    calificacion = models.FloatField(default=0)
    precio_inscripcion = models.DecimalField(max_digits=8, decimal_places=2)
    descripcion = models.TextField()
    vistas = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre_gym

class ClienteGimnasio(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='gimnasios_inscritos')
    gimnasio = models.ForeignKey(Gimnasio, on_delete=models.CASCADE, related_name='clientes')

    class Meta:
        unique_together = ('usuario', 'gimnasio')

    def __str__(self):
        return f"{self.usuario.email} inscrito en {self.gimnasio.nombre_gym}"

class Favorito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='favoritos')
    gimnasio = models.ForeignKey(Gimnasio, on_delete=models.CASCADE, related_name='favorito_por')

    class Meta:
        unique_together = ('usuario', 'gimnasio')

    def __str__(self):
        return f"{self.usuario.email} → {self.gimnasio.nombre_gym}"

class Rutina(models.Model):
    gimnasio = models.ForeignKey(Gimnasio, on_delete=models.CASCADE, related_name='rutinas')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.IntegerField(help_text="Duración en minutos")
    nivel = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
class Maquina(models.Model):
    gimnasio = models.ForeignKey(Gimnasio, on_delete=models.CASCADE, related_name='maquinas')
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre


class Inventario(models.Model):
    codigo_prod = models.AutoField(primary_key=True)
    gimnasio = models.ForeignKey(Gimnasio, on_delete=models.CASCADE, related_name='productos')
    nombre_prod = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nombre_prod
