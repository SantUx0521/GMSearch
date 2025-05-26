from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import (
    Usuario, Gimnasio, FichaBiometrica, ClienteGimnasio, Favorito,
    Rutina, Maquina, Inventario
)

# ------------------------
# Usuario (Registro Cliente)
# ------------------------
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'email', 'nombre', 'direccion', 'telefono', 'es_dueño', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, value):
        if Usuario.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este correo ya está registrado.")
        return value

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])
        return Usuario.objects.create(**validated_data)


# ------------------------
# Gimnasio
# ------------------------
class GimnasioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gimnasio
        fields = '__all__'


# ------------------------
# Favorito
# ------------------------
class FavoritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorito
        fields = '__all__'
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=Favorito.objects.all(),
                fields=['usuario', 'gimnasio'],
                message="Ya está marcado como favorito."
            )
        ]


# ------------------------
# Rutinas
# ------------------------
class RutinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rutina
        fields = '__all__'


# ------------------------
# Inventario
# ------------------------
class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = '__all__'


# ------------------------
# Maquinas
# ------------------------
class MaquinaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maquina
        fields = '__all__'
