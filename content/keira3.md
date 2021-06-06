title: Keira3 - Editor de bases de datos multiplataforma para AzerothCore
description: En este post, hablaremos sobre el editor llamado keira3, es un proyecto open source, con el cual puedes editar varias de las bases de datos de AzerothCore. Permitiéndote no solo ingresar nuevos valores, editarlos, eliminarlos, sino que también, obtener el SQL correspondiente que se ejecuta, para dicha acción.
date: 2021.06.06
authors: Pagani Walter
summary: Una buena alternativa, por si estas aprendiendo o no sabes SQL y queres editar las tablas del emulador de AzerothCore
category: Software
tags: basededatos, sql, azerothcore, keira3
repository: https://github.com/azerothcore/Keira3

![Keira3](https://raw.githubusercontent.com/azerothcore/Keira3/master/screenshot.png)

# Keira3

Aplicación de escritorio multiplataforma que incluye un **Editor de bases de datos** para el [AzerothCore](http://www.azerothcore.org).

Con Keira3 no tienes que conocer el lenguaje SQL para cambiar los contenidos: generará las consultas SQL automáticamente por ti. El código SQL se mostrará, para que puedas **aprender**, y luego podrás **copiarlo** o **ejecutarlo** directamente en tu base de datos.

Hecho con ❤ y [TypeScript](http://www.typescriptlang.org/), [Electron](https://electronjs.org/), [Angular](https://angular.io/), [Bootstrap](https://getbootstrap.com/).

## Apóyanos

Puedes apoyar el desarrollo de Keira3, realizando donaciones en [PayPal](https://www.paypal.me/francesco92dev).

## Inspirado por

Creamos Keira inspirándonos en el antiguo editor de bases de datos [indomit's Quice/Truice](https://github.com/indomit/quice) y en el [Discover-'s SAI Editor](https://github.com/jasperrietrae/SAI-Editor). Nuestro objetivo principal era proporcionar un editor con las mismas características que fuera multiplataforma, así que lo construimos como una aplicación web.

Keira3 es el sucesor directo de [Keira2](https://github.com/Helias/Keira2). Mantuvimos la promesa de multiplicidad de plataformas, además de añadir la posibilidad de ejecutar las consultas generadas y simplificar la configuración de la aplicación.

## Base de datos AzerothCore

Para utilizar Keira3 tienes que conectarte a una instancia de la base de datos de [AzerothCore](https://github.com/azerothcore/azerothcore-wotlk)

Si no tienes ninguno, puedes crear uno fácilmente siguiendo [esta guía](http://www.azerothcore.org/wiki/database-only-quick-setup).

Como alternativa, puedes utilizar una base de datos pública de AzerothCore con acceso de sólo lectura. Detalles [aquí](https://github.com/azerothcore/forum/issues/84).

## Cómo instalar Keira3

Para usar Keira3, no necesitas instalar ninguna dependencia. Basta con [descargar](https://github.com/azerothcore/Keira3/releases) y ejecutarlo.

Si utiliza Arch Linux, puede encontrar el paquete en [AUR](https://aur.archlinux.org/packages/keira3/)

Si está utilizando una base de datos `MySQL 8.0` puede encontrarse con este error:

_Client does not support authentication protocol requested by server; consider upgrading MySQL client_

Antes de registrarte con Keira recuerda ejecutar esta consulta en tu base de datos para los usuarios que desees:

```sql
ALTER USER 'acore' IDENTIFIED WITH mysql_native_password BY 'acore';
flush privileges;
```

[Más información sobre este tema aquí](https://stackoverflow.com/questions/50093144/mysql-8-0-client-does-not-support-authentication-protocol-requested-by-server)

### Aprende sobre Keira3

- Una visión general del funcionamiento interno de Keira3 está disponible [aquí](https://www.azerothcore.org/wiki/keira3-internals)
