# NomNom\! 

> **NomNom\!** es una solución *full-stack* diseñada para empoderar a **pequeños negocios locales** (taquerías, cafeterías, etc.) para gestionar sus **pedidos en línea** y **entregas a domicilio** directamente, eliminando la dependencia de costosas apps de terceros.

-----

## Módulos y Funcionalidades Clave

La plataforma está dividida en módulos clave para una operación digital completa:

| Rol | Módulo | Descripción |
| :--- | :--- | :--- |
| **Clientes** |  Catálogo y Carrito | Interfaz de compra fácil de usar y gestión del pedido. |
| **Clientes** |  Pedido y Seguimiento | Notificaciones en tiempo real y *tracking* de la entrega. |
| **Negocio** |  Panel Administrativo | Gestión de ventas, inventario (productos) y reportes. |
| **General** |  Versión Web | Acceso completo para clientes y administradores. |
| **General** |  Versión Móvil | Aplicaciones dedicadas para clientes y repartidores (*React Native*). |

-----

## Stack Tecnológico

**NomNom\!** está construido sobre tecnologías modernas y escalables:

| Componente | Tecnología | Notas |
| :--- | :--- | :--- |
| **Frontend Web** | **React** | Interfaz de administrador y tienda web. |
| **Frontend Móvil** | **React Native** | Apps para Repartidores y Clientes. |
| **Backend / API** | **Django** (Python) | Lógica de negocio, autenticación y gestión de datos. |
| **Base de Datos** | **PostgreSQL** | Base de datos relacional robusta y confiable. |
| **Hosting (Propuesto)** | **Render** o **Heroku** | Plataformas *PaaS* ideales para Django/React. |

-----

## Equipo de Desarrollo

Este proyecto es una colaboración de:

  * **Julio Emmanuel Romero Beltrán** ([@JulioRomeroBeltran][1])
  * **Jesus Gabriel Ruiz de Anda** ([@Quillet030][2])
  * **Ramón Alejandro Castro Noriega** ([@TakeshiPrime][3])
  * **Pablo Tadeo Torres Leal** ([@PTadeo][4])


[1]: https://github.com/JulioRomeroBeltran
[2]: https://github.com/Quillet030
[3]: https://github.com/TakeshiPrime
[4]: https://github.com/PTadeo


## Instalacion y configuracion del entorno

Para asegurar que todos los miembros del equipo puedan ejecutar **NomNom** con las mismas dependencias de Python y un entorno de trabajo consistente, sigue los pasos a continuación:

---

### 1. Clonar el Repositorio

Abre tu terminal o Git Bash y ejecuta los siguientes comandos para descargar el proyecto y navegar a su directorio:

```bash
git clone [https://github.com/JulioRomeroBeltran/NomNom.git](https://github.com/JulioRomeroBeltran/NomNom.git)
cd NamNam
```

### 2. Crear y Activar un Entorno Virtual

Es fundamental trabajar con un entorno virtual para aislar las dependencias del proyecto.

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Instalar las Dependencias

Con el entorno virtual activado, instala todas las librerías necesarias especificadas en el archivo requirements.txt:

```bash
pip install -r requirements.txt
```
Este paso instalará todas las librerías necesarias para que el proyecto funcione correctamente.
