import pytest
from django.test import TestCase
from rest_framework.test import APIClient
from core.models import Usuario





@pytest.mark.django_db
def test_registro_usuario_exitoso():
    client = APIClient()
    payload = {
        "email": "test@example.com",
        "nombre": "Juan Pérez",
        "direccion": "Calle Falsa 123",
        "telefono": "123456789",
        "es_dueño": False,
        "password": "mi_password123"
    }

    response = client.post("/registro/", payload)
    assert response.status_code == 201
    assert Usuario.objects.filter(email="test@example.com").exists()

#@pytest.mark.django_db
#def test_registro_usuario_email_duplicado():
 #   client = APIClient()
  #  Usuario.objects.create_user(
   #     email="test@example.com",
    #    nombre="Repetido",
     #   password="123"
    #)

    #payload = {
     #   "email": "test@example.com",
      #  "nombre": "Otro Nombre",
       # "direccion": "Otra Dirección",
        #"telefono": "111111111",
        #"es_dueño": False,
        #"password": "otra_pass"
    #}

    #response = client.post("/registro/", payload)
    #assert response.status_code == 400
    #assert "correo" in str(response.data).lower()

