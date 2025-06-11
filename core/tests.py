import pytest
from django.test import TestCase
from rest_framework.test import APIClient
from core.models import Usuario

import pytest
from core.models import Usuario
from django.contrib.auth.hashers import make_password

@pytest.fixture
def usuario_existente(db):
    return Usuario.objects.create(
        email="existente@example.com",
        nombre="Usuario Existente",
        direccion="Calle Real 456",
        telefono="987654321",
        es_dueño=False,
        password=make_password("passwordseguro")
    )


@pytest.mark.django_db
def test_registro_usuario_email_duplicado(usuario_existente):
    client = APIClient()
    payload = {
        "email": "existente@example.com",  # Mismo email que la fixture
        "nombre": "Otro Nombre",
        "direccion": "Otra Dirección",
        "telefono": "111111111",
        "es_dueño": False,
        "password": "otra_pass"
    }

    response = client.post("/api/registro/", payload)  # Usa el endpoint real
    assert response.status_code == 400
    assert "email" in str(response.data).lower()

@pytest.mark.django_db
def test_registro_usuario_email_duplicado():
    client = APIClient()
    Usuario.objects.create(
        email="duplicado@example.com",
        nombre="Usuario Duplicado",
        direccion="Calle 1",
        telefono="000000000",
        es_dueño=False,
        password=make_password("password123")  # encriptación manual
    )

    payload = {
        "email": "duplicado@example.com",
        "nombre": "Nuevo Nombre",
        "direccion": "Nueva Dirección",
        "telefono": "111111111",
        "es_dueño": False,
        "password": "otra_pass"
    }

    response = client.post("/api/registro/", payload)
    assert response.status_code == 400
    assert "email" in str(response.data).lower()
