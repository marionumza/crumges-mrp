=====================================
Cantidad Potencial de Fabricación MRP
=====================================

.. |badge1| image:: https://img.shields.io/badge/maturity-Beta-yellow.png
    :alt: Beta
.. |badge2| image:: https://img.shields.io/badge/license-AGPL--3-blue.png
    :alt: License: AGPL-3
.. |badge3| image:: https://img.shields.io/badge/github-Crumges%2Fmodules-lightgray.png?logo=github
    :alt: Crumges/modules
.. |badge4| image:: https://img.shields.io/badge/weblate-Translate%20me-F47D42.png
    :alt: Translate me on Weblate

|badge1| |badge2| |badge3| |badge4|

Muestra la cantidad potencial de stock a fabricar basándose en la disponibilidad de los componentes de la Lista de Materiales (BoM).

**Tabla de contenidos**

.. contents::
   :local:

Configuración
=============

No requiere configuración especial. Automáticamente calcula sobre los productos que tengan una Lista de Materiales (BoM) asignada.

Modo de Uso
===========

Este módulo añade indicadores visuales potentes tanto en la ficha del producto como en las vistas de tarjetas (Kanban) para ayudar a producción a tomar decisiones rápidas.

**Por qué y Para qué:**
Nativamente en Odoo, la función de "stock potencial" funciona bien para Listas de Materiales del tipo "Kit" (ya que un Kit no se almacena como tal, sino que es la suma de sus partes). Sin embargo, para productos de tipo "Fabricación" esto no funciona así: el producto final debe ser almacenable y nativamente Odoo requiere que exista una Orden de Fabricación confirmada para empezar a mostrar las reservas de esos componentes. 
En una fábrica o línea de ensamble, un producto almacenable puede marcar '0 unidades a mano'. Para saber cuántas podrías fabricar AHORA MISMO, deberías entrar al reporte de Estructura de Materiales e investigar si hay materia prima suficiente. Este módulo trae ese número mágico al frente: te dice instantáneamente tu 'Stock Potencial' cruzando las fórmulas de la BoM directamente sobre los componentes, sin necesidad de tener una orden de fabricación creada.

**Regla de Extensión:**
Nativamente, Odoo no muestra este indicador rápido de potencial de fabricación. El módulo inyecta campos computados, un Smart Button en la vista de formulario del producto, y un Badge (etiqueta) visual en la vista Kanban. Es estrictamente un módulo de visualización de backend y no altera las rutas lógicas de despacho o venta.

Caso de Uso
===========

1. El operario de taller entra a la vista de Productos y busca la 'Mesa de Roble'.
2. El stock actual marca '0 Unidades'.
3. Sin embargo, en la misma tarjeta Kanban hay una etiqueta brillante que indica 'Stock Potencial: 5'.
4. Esto significa que, sin salir de la pantalla, el operario sabe que hay suficiente madera, barniz y tornillos en el almacén para mandar a ensamblar 5 mesas inmediatamente. Al hacer clic en el botón inteligente, accede directamente a la confirmación de la Estructura de Materiales.


Historial de Cambios
====================

18.0.1.0.1 (2026-06-21)
-----------------------
* **Traducción**: Creación del README formal en español, estructuración del Caso de Uso e integración de reglas OCA.

Reporte de Errores
==================

Los errores se rastrean en `GitHub Issues <https://github.com/Crumges/issues>`_.
En caso de problemas, por favor compruebe allí si su incidencia ya ha sido reportada.

Créditos
========

Autores
-------

* Crumges

Colaboradores
-------------

* Crumges Team

Mantenedores
------------

.. image:: https://crumges.com/web/image/website/1/logo/Crumges%20Website?unique=c82f12a
   :alt: Crumges
   :target: https://crumges.com

Este módulo es mantenido por Crumges.
