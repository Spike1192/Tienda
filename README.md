# Sistema de Tienda

Este es un sistema de gestión de tienda desarrollado con Flask y PostgreSQL, que permite administrar productos, realizar ventas y generar reportes.

## Características

- Sistema de autenticación de usuarios
- Gestión de productos
- Proceso de pago
- Reportes de ventas
- Configuración del sistema

## Requisitos

- Python 3.x
- PostgreSQL
- Flask
- psycopg2

## Estructura del Proyecto

```
├── app.py              # Archivo principal de la aplicación
├── blueprints/         # Módulos de la aplicación
│   ├── bd01_login/    # Autenticación
│   ├── bd02_productos/# Gestión de productos
│   ├── bd03_pagar/    # Proceso de pago
│   ├── bd04_reporte_ventas/ # Reportes
│   └── bd05_configuracion/  # Configuración
├── modelos/           # Modelos de base de datos
├── static/           # Archivos estáticos (CSS, JS, imágenes)
└── templates/        # Plantillas HTML
```

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/Spike1192/Tienda.git
cd Tienda
```

2. Crear y activar un entorno virtual:

```bash
python -m venv entorno
# En Windows:
entorno\Scripts\activate
# En Linux/Mac:
source entorno/bin/activate
```

3. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

4. Configurar la base de datos PostgreSQL y actualizar la cadena de conexión en `modelos/modelo00_bd.py`

5. Ejecutar la aplicación:

```bash
python app.py
```

La aplicación estará disponible en `http://127.0.0.1:5000`

## Módulos Principales

### Login (bd01_login)

- Autenticación de usuarios
- Gestión de sesiones

### Productos (bd02_productos)

- Catálogo de productos
- Gestión de inventario

### Pago (bd03_pagar)

- Proceso de pago
- Gestión de transacciones

### Reportes (bd04_reporte_ventas)

- Generación de reportes de ventas
- Estadísticas

### Configuración (bd05_configuracion)

- Configuración del sistema
- Ajustes generales

## Tecnologías Utilizadas

- **Backend**: Flask (Python)
- **Base de Datos**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript
- **Framework CSS**: Bootstrap

## Contribución

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.
