#  GMSearch - Plataforma de Búsqueda de Gimnasios

Una aplicación web desarrollada en Django para buscar, gestionar y conectar usuarios con gimnasios.

##  Características

- **Registro y autenticación de usuarios** con verificación por email
- **Perfiles de usuario** con información personal y biométrica
- **Registro de gimnasios** para dueños
- **Búsqueda avanzada** de gimnasios por ubicación y características
- **Sistema de favoritos** para usuarios
- **Gestión de rutinas y máquinas** para gimnasios
- **Interfaz responsive** adaptada a todos los dispositivos

##  Despliegue en Heroku

### Prerrequisitos

1. **Cuenta de Heroku**: [Regístrate aquí](https://signup.heroku.com/)
2. **Heroku CLI**: [Descárgalo aquí](https://devcenter.heroku.com/articles/heroku-cli)
3. **Git**: Asegúrate de tener Git instalado
4. **SendGrid**: Cuenta para envío de emails

### Pasos para el despliegue

#### 1. Clonar el repositorio
```bash
git clone https://github.com/SantUx0521/Proyecto-pagina-de-gimnasio-.git
cd Proyecto-pagina-de-gimnasio-
```

#### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

#### 3. Configurar variables de entorno
Crea un archivo `.env` en la raíz del proyecto:
```env
SECRET_KEY=tu_secret_key_aqui
DEBUG=False
SENDGRID_API_KEY=tu_sendgrid_api_key
```

#### 4. Desplegar en Heroku

**Opción A: Usando el script automático**
```bash
chmod +x deploy.sh
./deploy.sh
```

**Opción B: Manual**
```bash
# Iniciar sesión en Heroku
heroku login

# Crear aplicación
heroku create tu-app-name

# Configurar variables de entorno
heroku config:set DEBUG=False
heroku config:set SENDGRID_API_KEY=tu_sendgrid_api_key

# Agregar base de datos PostgreSQL
heroku addons:create heroku-postgresql:mini

# Ejecutar migraciones
heroku run python manage.py migrate

# Desplegar
git push heroku main

# Abrir aplicación
heroku open
```

### Variables de entorno en Heroku

Configura estas variables en tu aplicación de Heroku:

- `SECRET_KEY`: Clave secreta de Django (se genera automáticamente)
- `DEBUG`: False para producción
- `SENDGRID_API_KEY`: Tu API key de SendGrid
- `DATABASE_URL`: URL de la base de datos PostgreSQL (se configura automáticamente)

##  Desarrollo Local

### Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/SantUx0521/Proyecto-pagina-de-gimnasio-.git
cd Proyecto-pagina-de-gimnasio-
```

2. **Crear entorno virtual**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Configurar variables de entorno**
Crea un archivo `.env` en la raíz:
```env
SECRET_KEY=tu_secret_key_aqui
DEBUG=True
SENDGRID_API_KEY=tu_sendgrid_api_key_aqui
```

5. **Ejecutar migraciones**
```bash
python manage.py migrate
```

6. **Crear superusuario (opcional)**
```bash
python manage.py createsuperuser
```

7. **Ejecutar servidor**
```bash
python manage.py runserver
```

La aplicación estará disponible en `http://localhost:8000`

##  Estructura del Proyecto

```
Proyecto-pagina-de-gimnasio-/
├── backend/                 # Configuración principal de Django
│   ├── settings.py         # Configuración del proyecto
│   ├── urls.py             # URLs principales
│   └── wsgi.py             # Configuración WSGI
├── core/                   # Aplicación principal
│   ├── models.py           # Modelos de datos
│   ├── views.py            # Vistas y lógica de negocio
│   ├── urls.py             # URLs de la aplicación
│   ├── templates/          # Plantillas HTML
│   └── static/             # Archivos estáticos (CSS, JS, imágenes)
├── media/                  # Archivos subidos por usuarios
├── requirements.txt        # Dependencias de Python
├── Procfile               # Configuración para Heroku
├── runtime.txt            # Versión de Python
├── app.json               # Configuración de Heroku
└── .env                   # Variables de entorno (no subir al repositorio)
```

##  Tecnologías Utilizadas

- **Backend**: Django 4.2+
- **Base de datos**: SQLite (desarrollo) / PostgreSQL (producción)
- **Frontend**: HTML5, CSS3, JavaScript
- **Email**: SendGrid
- **Despliegue**: Heroku
- **Archivos estáticos**: WhiteNoise

##  Configuración de Email

El proyecto usa SendGrid para el envío de emails. Para configurarlo:

1. Crea una cuenta en [SendGrid](https://sendgrid.com/)
2. Genera una API Key
3. Configura la variable `SENDGRID_API_KEY` en tu entorno

##  Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

##  Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

##  Autores

- *Desarrollo inicial* - [SantUx0521](https://github.com/SantUx0521)
 - **Miguel Angel Arboleda – 2160253**
 - **Alejandro Garzon – 2266088**
 - **Santiago Useche Tascón – 2266200**
##  Agradecimientos

- Django Documentation
- Heroku Documentation
- SendGrid Documentation
- Comunidad de desarrolladores de Python

---

**¡Gracias por usar GMSearch!**
