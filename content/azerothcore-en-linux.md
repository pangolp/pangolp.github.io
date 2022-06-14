title: Compilar AzerothCore en Linux
description: En esta guía, simplemente queremos mostrar una forma diferente de compilar AzerothCore desde cero, paso a paso, en Debian y Ubuntu. Siempre recuerden revisar la documentación oficial, la cual se encuentra en la wiki de la comunidad.
date: 2022.06.12
authors: Pagani Walter
summary: En esta guía, simplemente queremos mostrar una forma diferente de compilar AzerothCore desde cero, paso a paso, en Debian y Ubuntu. Siempre recuerden revisar la documentación oficial, la cual se encuentra en la wiki de la comunidad.
category: Emuladores de World of Warcraft
tags: azerothcore, server335, linux
repository: https://github.com/azerothcore/azerothcore-wotlk

### ¿Qué necesito instalar?

Antes que nada, debemos saber, que al día de la fecha: Domingo 12 de Junio del 2022, aun el emulador, no soporta versiones de OpenSSL 3.x. Por lo que no podemos usar la versión de Ubuntu 22.04, dado que esta, por defecto en sus repositorios, viene con dicha versión de OpenSSL. Sin embargo, podríamos usar esta versión de Ubuntu, es decir, la 22.04, desinstalar OpenSSL que viene por defecto / no instarlo, y luego descargar una versión del código de la versión 1.1.x, y compilarlo nosotros mismo. Mi recomendación, utilicen una versión de Ubuntu anterior, como puede ser la versión 21.10 (la cual no esta tan desactualizada).

<details>
<summary>Ubuntu con MariaDB 10.x</summary>
AzerothCore sólo es compatible con las versiones 10.5 y 10.6 de MariaDB.

```sh
sudo apt update && sudo apt full-upgrade -y && sudo apt install git cmake make gcc g++ clang libssl-dev libbz2-dev libreadline-dev libncurses-dev libboost-all-dev mariadb-server mariadb-client libmariadb-dev libmariadb-dev-compat -y
```

</details>

<details>
<summary>Ubuntu con MySQL 8.x</summary>

```sh
sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang libmysqlclient-dev libssl-dev libbz2-dev libreadline-dev libncurses-dev mysql-server libboost-all-dev -y
```

</details>

<details>
<summary>Debian 10 / Debian 11</summary>

```sh
sudo apt-get update && sudo apt-get install git cmake make gcc g++ clang default-libmysqlclient-dev libssl-dev libbz2-dev libreadline-dev libncurses-dev mariadb-server libboost-all-dev -y
```

</details>
<br>

### Clonar del repositorio y compilación

En este ejemplo práctico, voy a hacer uso de la consola. Y tomando la información de la wiki, vemos que tenemos 3 formas de clonar el repositorio.

Antes de continuar, tendríamos que crear un usuario donde realizamos la instalación. Lo haremos, mediante el comando `adduser`. Siendo root, o con permisos de sudo, creamos un usuario llamado wow, por ejemplo, de la siguiente manera: `adduser wow`. Luego de darle entender, nos pedirá una contraseña, la cual tendremos que introducir 2 veces y otros datos personales, los cuales realmente no tienen demasiada importancia, podemos dejarlos vacío, pulsando varias veces enter, y luego, al final, confirmamos escribiendo Y.

Una vez, hayamos creado el usuario, podemos iniciar sección con él, o podemos cambiar de usuario, escribiendo `su – wow`. El cual, si estamos con el usuario root, no nos pedirá la contraseña, pero si estamos con otro usuario sí. Estando dentro del `/home` del usuario, que sería: `/home/wow` (lo cual podemos comprobar con la ayuda del comando `pwd`, disponemos de clonar el repositorio dentro del home de dicho usuario (wow). El home, es la carpeta persona del usuario, podríamos hacerlo en otro lugar también, pero a efectos prácticos, lo vamos a hacer dentro del home del usuario.

<details>
<summary>Rama master con el historial completo (tamaño más pequeño - recomendado):</summary>

```sh
git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore
```

</details>

<details>
<summary>Rama maestra sin historial previo (tamaño más pequeño):</summary>

```sh
git clone https://github.com/azerothcore/azerothcore-wotlk.git --branch master --single-branch azerothcore --depth 1
```

</details>

<details>
<summary>Todas las ramas y todo el historial:</summary>

```sh
git clone https://github.com/azerothcore/azerothcore-wotlk.git azerothcore
```

</details>
<br>
Una vez realizada la clonación, comienza la compilación.

A continuación, vamos a ingresar en el directorio llamado AzerothCore, y dentro de él, crear una carpeta llamada build y luego, ingresar dentro de la carpeta. Para eso, podemos ejecutar los pasos por separado. O podemos hacerlo todo en una línea, le dejo ambos métodos, para que ustedes elijan.

<details>
<summary>Por separado</summary>

```sh
cd azerothcore
mkdir build
cd build
```

</details>

<details>
<summary>Todo junto</summary>

```sh
cd azerothcore && mkdir build && cd build
```

</details>
<br>
Ambos métodos son válidos, y dependiendo de donde nos encontramos, podremos obtener resultados distintos. Les recomiendo siempre revisar donde están parados, haciendo uso del comando `pwd`. O incluso, para asegurarse, si están usando el usuario `wow` pueden ir al `home` del usuario, escribiendo `cd $HOME`. $HOME es una variable de entorno, que apunta a la carpeta personal del usuario que tiene la sección activa, en este caso, `wow`.

Es hora de ponerse a compilar…

Para eso, primero debemos construir la solución de lo que vamos a compilar, con cmake. El comando cmake, tiene varios parámetros, por lo que vamos a publicar a continuación, es una forma de hacerlo, pero no es la única. Revisen siempre la guía del comando, para obtener más información sobre el mismo, y los diferentes parámetros que tiene.

<details>
<summary>Cmake para construir la solución</summary>

```sh
cmake ../ -DCMAKE_INSTALL_PREFIX=$HOME/azeroth-server/ -DCMAKE_C_COMPILER=/usr/bin/clang -DCMAKE_CXX_COMPILER=/usr/bin/clang++ -DWITH_WARNINGS=1 -DTOOLS=0 -DSCRIPTS=static -DMODULES=static
```

</details>
<br>

<details>
<summary>Ejemplo de lo que obtenemos al usar el comando anterior</summary>

```sh
-- CMake version: 3.18.4
-- Running cmake hook: AFTER_LOAD_CONF
-- No hooks registered for AFTER_LOAD_CONF
-- Enabled С++20 standard
-- Detected 64-bit platform
-- UNIX: Using jemalloc
-- UNIX: Using default configuration directory
-- UNIX: Using default library directory
-- UNIX: Configuring uninstall target
-- UNIX: Created uninstall target
-- UNIX: Detected compiler: /usr/bin/clang
-- Clang: Minimum version required is 10.0.0, found 11.0.1 - ok!
-- Clang: All warnings enabled
-- Running cmake hook: AFTER_LOAD_CMAKE_MODULES
-- No hooks registered for AFTER_LOAD_CMAKE_MODULES
-- Using mysql-config: /usr/bin/mysql_config
-- Found MySQL library: /usr/lib/x86_64-linux-gnu/libmariadb.so
-- Found MySQL headers: /usr/include/mariadb
-- Found MySQL executable: /usr/bin/mysql
-- Found git binary : /usr/bin/git

* AzerothCore revision            : b004f9883e12 2022-06-04 00:26:02 +0000 (master branch)
* AzerothCore buildtype           : RelWithDebInfo

* Install core to                 : /home/wow/azeroth-server
* Install libraries to            : /home/wow/azeroth-server/lib
* Install configs to              : /home/wow/azeroth-server/etc

* Build applications              : Yes (all)
* Build tools                     : No
* Build with scripts              : Yes (static)
* Build with modules              : Yes (static)
* Build unit tests                : No  (default)
* Build core w/PCH                : Yes (default)
* Build scripts w/PCH             : Yes (default)
* Show all warnings               : Yes
* Use coreside debug              : No  (default)
* Use unix gperftools             : No  (default)
* Use GIT revision hash           : Yes (default)
* Enable vmap DisableMgr checks   : Yes (default)
* Show source tree                : No (For UNIX default)

-- Found Readline library: /usr/lib/x86_64-linux-gnu/libreadline.so
-- Include dir is: /usr/include
-- Running cmake hook: BEFORE_SRC_LOAD
-- No hooks registered for BEFORE_SRC_LOAD

* Apps build list (all):
  |
  +- apps
  |   +- authserver
  |   +- worldserver
  |

-- Running cmake hook: BEFORE_GAME_LIBRARY
-- No hooks registered for BEFORE_GAME_LIBRARY
-- Running cmake hook: AFTER_GAME_LIBRARY
-- No hooks registered for AFTER_GAME_LIBRARY
-- Running cmake hook: BEFORE_SCRIPTS_LIBRARY
-- No hooks registered for BEFORE_SCRIPTS_LIBRARY
* Script configuration (static):
  |
  +- worldserver
  |   +- Commands
  |   +- Custom
  |   +- EasternKingdoms
  |   +- Events
  |   +- Kalimdor
  |   +- Northrend
  |   +- OutdoorPvP
  |   +- Outland
  |   +- Pet
  |   +- Spells
  |   +- World
  |


* Modules configuration (static):
  |

-- * Modules config list:
  |

-- Running cmake hook: AFTER_SRC_LOAD
-- No hooks registered for AFTER_SRC_LOAD
-- Configuring done
-- Generating done
-- Build files have been written to: /home/wow/azerothcore/build
```

</details>
<br>
Luego, de hacer uso del comando, podemos empezar a compilar, pero para ello, necesitamos saber cuántos núcleos, tenemos disponibles. Eso podemos hacerlo, con el comando `nproc –all`. Básicamente, lo que nos va a aparecer en pantalla, es la cantidad de núcleos, que podemos usar. A efectos prácticos, voy a usar 6 núcleos. Por lo que el comando, que debo usar para compilar es:

<details>
<summary>Comando make</summary>

```sh
make -j 6 && make install
```

</details>
<br>
Al finalizar la compilación, obtendrán un resultado como este

<details>
<summary>Resultado</summary>

```sh
[  1%] Built target argon2
[  1%] Built target fmt
[  1%] Built target Detour
[  1%] Built target sfmt
[  5%] Built target g3dlib
[  6%] Built target gsoap
[  7%] Built target Recast
[ 10%] Built target jemalloc
[ 16%] Built target common
[ 18%] Built target database
[ 19%] Built target shared
[ 19%] Built target revision.h
[ 19%] Built target modules
[ 19%] Built target authserver
[ 45%] Built target game
[ 99%] Built target scripts
[100%] Built target worldserver
[  0%] Built target sfmt
[  1%] Built target argon2
[  1%] Built target fmt
[  4%] Built target jemalloc
[  8%] Built target g3dlib
[  8%] Built target Detour
[  9%] Built target Recast
[ 10%] Built target gsoap
[ 16%] Built target common
[ 16%] Built target revision.h
[ 18%] Built target database
[ 19%] Built target shared
[ 19%] Built target modules
[ 45%] Built target game
[ 99%] Built target scripts
[100%] Built target worldserver
[100%] Built target authserver
Install the project...
-- Install configuration: "RelWithDebInfo"
-- Up-to-date: /home/wow/azeroth-server/etc/authserver.conf.dist
-- Up-to-date: /home/wow/azeroth-server/etc/worldserver.conf.dist
```

</details>
