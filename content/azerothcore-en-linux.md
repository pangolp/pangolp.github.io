title: Compilar AzerothCore en Linux
description: En esta guía, simplemente queremos mostrar una forma diferente de compilar AzerothCore desde cero, paso a paso, en Debian y Ubuntu. Siempre recuerden revisar la documentación oficial, la cual se encuentra en la wiki de la comunidad.
date: 2022.06.12
authors: Pagani Walter
summary: En esta guía, simplemente queremos mostrar una forma diferente de compilar AzerothCore desde cero, paso a paso, en Debian y Ubuntu. Siempre recuerden revisar la documentación oficial, la cual se encuentra en la wiki de la comunidad.
category: Emuladores de World of Warcraft
tags: azerothcore, server335, linux
repository: https://github.com/azerothcore/azerothcore-wotlk

<details>
    <summary>¿Qué necesito instalar?</summary>
    Antes que nada, debemos saber, que al día de la fecha: Domingo 12 de Junio del 2022, aun el emulador, no soporta versiones de OpenSSL 3.x. Por lo que no podemos usar la versión de Ubuntu 22.04, dado que esta, por defecto en sus repositorios, viene con dicha versión de OpenSSL. Sin embargo, podríamos usar esta versión de Ubuntu, es decir, la 22.04, desinstalar OpenSSL que viene por defecto / no instarlo, y luego descargar una versión del código de la versión 1.1.x, y compilarlo nosotros mismo. Mi recomendación, utilicen una versión de Ubuntu anterior, como puede ser la versión 21.10 (la cual no esta tan desactualizada).
</details>

<details>
    <summary>Ubuntu con MariaDB 10.x</summary>
    AzerothCore sólo es compatible con las versiones 10.5 y 10.6 de MariaDB.
    ```ssh
    sudo apt update && sudo apt full-upgrade -y && sudo apt install git cmake make gcc g++ clang libssl-dev libbz2-dev libreadline-dev libncurses-dev libboost-all-dev mariadb-server mariadb-client libmariadb-dev libmariadb-dev-compat -y
    ```
</details>

<details>
    <summary>Ubuntu con MySQL 8.x</summary>
    ```bash
    sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang libmysqlclient-dev libssl-dev libbz2-dev libreadline-dev libncurses-dev mysql-server libboost-all-dev -y
    ```
</details>

<details>
    <summary>Debian 10 / Debian 11</summary>
    ```bash
    sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang default-libmysqlclient-dev libssl-dev libbz2-dev libreadline-dev libncurses-dev mariadb-server libboost-all-dev -y
    ```
</details>
