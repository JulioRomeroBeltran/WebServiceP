# 🚀 NomNom\! ☁️

> **NomNom\!** es una solución *full-stack* diseñada para empoderar a **pequeños negocios locales** (taquerías, cafeterías, etc.) para gestionar sus **pedidos en línea** y **entregas a domicilio** directamente, eliminando la dependencia de costosas apps de terceros.

-----

## ✨ Módulos y Funcionalidades Clave

La plataforma está dividida en módulos clave para una operación digital completa:

| Rol | Módulo | Descripción |
| :--- | :--- | :--- |
| **Clientes** | 🛍️ Catálogo y Carrito | Interfaz de compra fácil de usar y gestión del pedido. |
| **Clientes** | 🛵 Pedido y Seguimiento | Notificaciones en tiempo real y *tracking* de la entrega. |
| **Negocio** | 🖥️ Panel Administrativo | Gestión de ventas, inventario (productos) y reportes. |
| **General** | 🌐 Versión Web | Acceso completo para clientes y administradores. |
| **General** | 📱 Versión Móvil | Aplicaciones dedicadas para clientes y repartidores (*React Native*). |

-----

## 💻 Stack Tecnológico

**LocalGo\!** está construido sobre tecnologías modernas y escalables:

| Componente | Tecnología | Notas |
| :--- | :--- | :--- |
| **Frontend Web** | **React** | Interfaz de administrador y tienda web. |
| **Frontend Móvil** | **React Native** | Apps para Repartidores y Clientes. |
| **Backend / API** | **Django** (Python) | Lógica de negocio, autenticación y gestión de datos. |
| **Base de Datos** | **PostgreSQL** | Base de datos relacional robusta y confiable. |
| **Hosting (Propuesto)** | **Render** o **Heroku** | Plataformas *PaaS* ideales para Django/React. |

-----

## 👥 Equipo de Desarrollo

Este proyecto es una colaboración de:

  * **Julio Emmanuel Romero Beltrán** ([@JulioRomeroBeltran][1])
  * **Jesus Gabriel Ruiz de Anda** ([@Quillet030][2])
  * **Ramón Alejandro Castro Noriega** ([@TakeshiPrime][3])
  * **Pablo Tadeo Torres Leal** ([@PTadeo][4])

-----

## ⚙️ Configuración y Despliegue Local

Para configurar y ejecutar el proyecto en tu entorno local, sigue los pasos de configuración para cada componente:

### 1\. Requisitos Previos

Asegúrate de tener instalado:

  * [Node.js](https://nodejs.org/en/) y npm
  * [Python 3.x](https://www.python.org/downloads/)
  * [PostgreSQL](https://www.postgresql.org/download/)

### 2\. Backend (Django)

1.  Clona el repositorio: `git clone [URL_DEL_REPO]`
2.  Ve al directorio del backend: `cd LocalGo/backend`
3.  Crea un entorno virtual y activa: `python -m venv venv && source venv/bin/activate`
4.  Instala dependencias: `pip install -r requirements.txt`
5.  Configura tu base de datos **PostgreSQL** y actualiza el archivo `.env` o `settings.py`.
6.  Aplica migraciones: `python manage.py migrate`
7.  Inicia el servidor: `python manage.py runserver`

### 3\. Frontend Web (React)

1.  Ve al directorio del frontend: `cd LocalGo/frontend-web`
2.  Instala dependencias: `npm install`
3.  Inicia la aplicación: `npm start`

-----

## 🤝 Contribuciones

Si tienes ideas o deseas mejorar **LocalGo\!**, ¡tu ayuda es bienvenida\!

1.  Haz un *fork* del repositorio.
2.  Crea una nueva rama para tu *feature* (`git checkout -b feature/nueva-funcionalidad`).
3.  Haz *commit* de tus cambios (`git commit -m 'feat: Añade nueva funcionalidad X'`).
4.  Haz *push* a la rama (`git push origin feature/nueva-funcionalidad`).
5.  Abre un *Pull Request* (PR).

-----

## 📜 Licencia

Este proyecto está bajo la Licencia **MIT**. Consulta el archivo `LICENSE` para más detalles.

[1]: https://www.google.com/search?q=%5Bhttps://github.com/JulioRomeroBeltran%5D\(https://github.com/JulioRomeroBeltran\)
[2]: https://www.google.com/search?q=%5Bhttps://github.com/Quillet030%5D\(https://github.com/Quillet030\)
[3]: https://github.com/TakeshiPrime
[4]: https://github.com/PTadeo
