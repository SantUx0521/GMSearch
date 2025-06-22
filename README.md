# GMSearch - Plataforma de Búsqueda de Gimnasios


Una aplicación web desarrollada en Django para buscar, gestionar y conectar usuarios con gimnasios.

## Características

- **Registro y autenticación de usuarios** con verificación por email
- **Perfiles de usuario** con información personal y biométrica
- **Registro de gimnasios** para dueños
- **Búsqueda avanzada** de gimnasios por ubicación y características
- **Sistema de favoritos** para usuarios
- **Gestión de rutinas y máquinas** para gimnasios
- **Interfaz responsive** adaptada a todos los dispositivos

##   Despliegue Rápido en Railway

### Para usar la página online inmediatamente:

1. **Ve a [Railway.app](https://railway.app)**
2. **Conecta tu cuenta de GitHub**
3. **Selecciona este repositorio**
4. **Railway detectará automáticamente que es un proyecto Django**
5. **Configura las variables de entorno:**
   ```
   SENDGRID_API_KEY=tu_api_key_de_sendgrid
   DEBUG=False
   ```
6. **¡Listo!** Tu página estará online en minutos

**No necesitas instalar Python, Django ni nada más.**

### Variables de entorno en Railway

Railway configurará automáticamente:
- `SECRET_KEY`: Se genera automáticamente
- `DATABASE_URL`: URL de PostgreSQL (se configura automáticamente)
- `PORT`: Puerto del servidor (se configura automáticamente)

Solo necesitas configurar:
- `SENDGRID_API_KEY`: Tu API key de SendGrid para emails
- `DEBUG`: False para producción

##  Desarrollo Local

### Si quieres modificar el código:

#### Prerrequisitos
- Python 3.11 o superior
- Git

#### Instalación

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
SECRET_KEY=django-insecure-+-*f3=(6=ftg9wh1oyij6_+)a!(#3m^%ovepdh8_r=a^2x$ja-
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
├── railway.json            # Configuración para Railway
├── runtime.txt             # Versión de Python
└── .env                    # Variables de entorno (no subir al repositorio)
```

##  Tecnologías Utilizadas

- **Backend**: Django 4.2+
- **Base de datos**: SQLite (desarrollo) / PostgreSQL (producción)
- **Frontend**: HTML5, CSS3, JavaScript
- **Email**: SendGrid
- **Despliegue**: Railway
- **Archivos estáticos**: WhiteNoise

##  Configuración de Email

El proyecto usa SendGrid para el envío de emails. Para configurarlo:

1. Crea una cuenta en [SendGrid](https://sendgrid.com/)
2. Genera una API Key
3. Configura la variable `SENDGRID_API_KEY` en Railway

##  Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

##  Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

##  Autores

- **Alejandro Garzon** - *Desarrollo inicial* - [SantUx0521](https://github.com/SantUx0521)

## Agradecimientos

- Django Documentation
- Railway Documentation
- SendGrid Documentation
- Comunidad de desarrolladores de Python

---

**¡Gracias por usar GMSearch!**
