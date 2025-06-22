# Panel de Administrador - GMSearch

## Descripción

El panel de administrador permite gestionar usuarios y gimnasios de la plataforma GMSearch desde una interfaz web intuitiva y segura.

## Características

### Panel Principal
- **Estadísticas en tiempo real**: Total de usuarios, gimnasios, usuarios verificados y pendientes
- **Navegación rápida**: Acceso directo a las diferentes secciones de gestión
- **Interfaz moderna**: Diseño responsive y fácil de usar

### Gestión de Usuarios
- **Lista completa**: Ver todos los usuarios registrados
- **Filtros avanzados**: Filtrar por estado (verificados, pendientes, dueños)
- **Búsqueda**: Buscar usuarios por nombre o email
- **Edición completa**: Modificar todos los datos del usuario
- **Gestión de permisos**: Activar/desactivar cuentas, cambiar roles
- **Eliminación segura**: Confirmación antes de eliminar usuarios

### Gestión de Gimnasios
- **Lista completa**: Ver todos los gimnasios registrados
- **Filtros**: Filtrar por disponibilidad de imágenes
- **Búsqueda**: Buscar por nombre, ubicación o dueño
- **Edición completa**: Modificar información del gimnasio
- **Estadísticas**: Ver calificaciones, reseñas y vistas
- **Eliminación segura**: Confirmación antes de eliminar gimnasios

## Instalación y Configuración

### 1. Crear un Usuario Administrador

Para crear un usuario administrador, ejecuta el siguiente comando:

```bash
python manage.py create_admin --email admin@ejemplo.com --nombre "Administrador" --password "contraseña123"
```

### 2. Acceder al Panel

1. Inicia sesión con las credenciales del administrador
2. Ve a tu perfil (botón "Ver perfil")
3. Serás redirigido automáticamente al panel de administrador

### 3. URLs del Panel

- **Panel principal**: `/admin-panel/`
- **Gestión de usuarios**: `/admin-panel/usuarios/`
- **Gestión de gimnasios**: `/admin-panel/gimnasios/`

## Funcionalidades Detalladas

### Gestión de Usuarios

#### Ver Usuarios
- Accede a `/admin-panel/usuarios/`
- Usa los filtros para encontrar usuarios específicos:
  - **Todos**: Muestra todos los usuarios
  - **Verificados**: Solo usuarios con email verificado
  - **Pendientes**: Solo usuarios sin verificar
  - **Dueños**: Solo dueños de gimnasios

#### Editar Usuario
1. Haz clic en el botón ✏️ junto al usuario
2. Modifica los campos necesarios:
   - Información personal (nombre, email, edad, etc.)
   - Información de contacto (teléfono, dirección)
   - Foto de perfil
   - Configuración de cuenta (permisos, estado)
3. Haz clic en "Guardar Cambios"

#### Eliminar Usuario
1. Haz clic en el botón 🗑️ junto al usuario
2. Confirma la eliminación
3. **⚠️ Atención**: Esta acción elimina todos los datos asociados

### Gestión de Gimnasios

#### Ver Gimnasios
- Accede a `/admin-panel/gimnasios/`
- Usa los filtros para encontrar gimnasios específicos:
  - **Todos**: Muestra todos los gimnasios
  - **Con imágenes**: Solo gimnasios con fotos
  - **Sin imágenes**: Solo gimnasios sin fotos

#### Editar Gimnasio
1. Haz clic en el botón ✏️ junto al gimnasio
2. Modifica los campos necesarios:
   - Información básica (nombre, ubicación, precio)
   - Estadísticas (calificación, reseñas, vistas)
   - Descripción
   - Imagen del gimnasio
3. Haz clic en "Guardar Cambios"

#### Eliminar Gimnasio
1. Haz clic en el botón 🗑️ junto al gimnasio
2. Confirma la eliminación
3. **⚠️ Atención**: Esta acción elimina todos los datos asociados

## Seguridad

### Permisos Requeridos
- Solo usuarios con `is_staff = True` pueden acceder al panel
- Los administradores no pueden eliminarse a sí mismos
- Todas las acciones requieren confirmación

### Validaciones
- Verificación de permisos en cada vista
- Confirmación antes de eliminaciones
- Validación de datos en formularios

## Interfaz de Usuario

### Diseño Responsive
- Funciona en dispositivos móviles y de escritorio
- Navegación intuitiva con iconos
- Colores consistentes y accesibles

### Elementos Visuales
- **Badges de estado**: Verde para verificados, amarillo para pendientes
- **Badges de tipo**: Diferentes colores para admin, dueño, usuario
- **Estrellas**: Visualización de calificaciones
- **Iconos**: Emojis para mejor identificación

## Comandos Útiles

### Crear Administrador
```bash
python manage.py create_admin --email admin@ejemplo.com --nombre "Administrador" --password "contraseña123"
```

### Verificar Usuarios Pendientes
```bash
python manage.py shell
```
```python
from core.models import Usuario
pendientes = Usuario.objects.filter(email_verificado=False)
print(f"Usuarios pendientes: {pendientes.count()}")
```

## Solución de Problemas

### No puedo acceder al panel
- Verifica que tu usuario tenga `is_staff = True`
- Asegúrate de estar logueado
- Revisa que la URL sea correcta

### No veo todos los usuarios/gimnasios
- Usa los filtros de búsqueda
- Verifica que no haya filtros activos
- Revisa la paginación si hay muchos registros

### Error al eliminar
- Verifica que no estés intentando eliminarte a ti mismo
- Asegúrate de confirmar la eliminación
- Revisa los logs del servidor

## Mantenimiento

### Respaldos
- Realiza respaldos regulares de la base de datos
- Documenta cambios importantes
- Mantén un registro de acciones administrativas

### Monitoreo
- Revisa regularmente las estadísticas del panel
- Monitorea usuarios pendientes de verificación
- Verifica la integridad de los datos

## Contacto y Soporte

Para reportar problemas o solicitar nuevas funcionalidades:
- Revisa la documentación del proyecto
- Consulta los logs del servidor
- Contacta al equipo de desarrollo

---

**Nota**: Este panel está diseñado para uso administrativo. Usa con responsabilidad y siempre confirma las acciones importantes antes de ejecutarlas. 