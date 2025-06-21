#!/bin/bash

echo " Iniciando despliegue en Heroku..."

# Verificar que Heroku CLI esté instalado
if ! command -v heroku &> /dev/null; then
    echo " Heroku CLI no está instalado. Por favor instálalo desde: https://devcenter.heroku.com/articles/heroku-cli"
    exit 1
fi

# Verificar que estés logueado en Heroku
if ! heroku auth:whoami &> /dev/null; then
    echo " Por favor inicia sesión en Heroku:"
    heroku login
fi

# Crear aplicación en Heroku (si no existe)
echo " Creando aplicación en Heroku..."
heroku create gymsearch-app --buildpack heroku/python

# Configurar variables de entorno
echo " Configurando variables de entorno..."
heroku config:set DEBUG=False
heroku config:set SENDGRID_API_KEY=$SENDGRID_API_KEY

# Agregar base de datos PostgreSQL
echo " Configurando base de datos PostgreSQL..."
heroku addons:create heroku-postgresql:mini

# Ejecutar migraciones
echo " Ejecutando migraciones..."
heroku run python manage.py migrate

# Crear superusuario (opcional)
echo " ¿Quieres crear un superusuario? (y/n)"
read -r response
if [[ "$response" =~ ^([yY][eE][sS]|[yY])$ ]]; then
    heroku run python manage.py createsuperuser
fi

# Desplegar aplicación
echo " Desplegando aplicación..."
git push heroku main

# Abrir aplicación
echo " Abriendo aplicación..."
heroku open

echo " ¡Despliegue completado!"
echo " Tu aplicación está disponible en: https://gymsearch-app.herokuapp.com" 