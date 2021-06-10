title: Cómo probar un Pull Request
description: En este post, hablamos sobre cómo realizar pruebas de las solicitudes de cambios (PR – Pull request), como también así, de la importancia que la misma tiene para cualquier proyecto open source.
date: 2021.06.10
authors: Pagani Walter
summary: Hablemos sobre los Pull Request
category: Github
tags: azerothcore, github, pullrequest, testing

### Introducción

En AzerothCore nos preocupamos por la calidad y la estabilidad del juego. Por ello, **no enviamos los cambios directamente a la rama maestra (master)**. En su lugar, cada vez que introducimos un nuevo cambio, creamos un nuevo [Pull Request](https://help.github.com/articles/about-pull-requests/){:target="_blank"} (a menudo acortado en PR). Esto nos permite **revisar y probar** adecuadamente cualquier cambio antes de que llegue a los entornos de producción. Todos los que pueden instalar AzerothCore también pueden contribuir probando los PR. Esta guía explicará cómo hacerlo. Cuantos más usuarios nos ayuden a probar los PRs, mejor será nuestra actividad de desarrollo en términos de velocidad y calidad.

### ¿Qué PRs necesitan ser probados?

Etiquetamos como [Esperando ser probado](https://github.com/azerothcore/azerothcore-wotlk/pulls?q=is%3Apr+is%3Aopen+label%3A%22Waiting+to+be+tested%22){:target="_blank"} a todos los PRs que ya han sido completados por el autor y han tenido su código revisado. Al hacer clic en la etiqueta anterior, se mostrará la lista de todos los PR que deben probarse para llegar a la rama maestra (master). **Es importante que la comunidad ayude a testear, porque si los desarrolladores suben un cambio, y el mismo esta mucho tiempo sin revisarse, pueden perder un poco la motivación por seguir colaborando.**

### ¿Qué necesito antes de probar un PR?

Es necesario:

- Tener AzerothCore instalado en tu sistema (ver [Instalación](https://www.azerothcore.org/wiki/Installation){:target="_blank"}).
- Tener una cuenta en GitHub, puedes [registrar una aquí](https://github.com/join){:target="_blank"} de forma gratuita.

### ¿Y si el PR sólo tiene cambios en la base de datos?

Algunos PRs sólo tienen cambios en la base de datos (sin cambios en C++). Si ese es el caso, hay un procedimiento [simplificado para probar esos cambios](https://www.azerothcore.org/wiki/How-to-test-DB-only-changes){:target="_blank"}. Si no estás seguro, sigue leyendo aquí y haz la prueba tradicional de PR que funcionará para todo tipo de PRs.

### Pasos para probar un pull request

- Debes tener un fork del repositorio y haberlo clonado.

![fork](https://user-images.githubusercontent.com/2810187/121466203-67901680-c98d-11eb-9257-1f8fcc439cfc.png)

- El siguiente paso, es diferente, si eres **colaborador** a si solo vas a ser **tester**. Si eres colaborador, debes añadir una referencia a AzerothCore, llamada comúnmente como **upstream**. Dado que al clonar el repositorio, tu repositorio remoto es el origin. Si solo vas a realizar pruebas, no necesitas hacer el paso anterior. En mi caso, yo a haces hago algún que otro PR, como también intento testear los que hacen otros colaboradores. Por lo que debo tener ambas referencias, como en la imagen que se muestra a continuación.

![remotes](https://user-images.githubusercontent.com/2810187/121466589-0d438580-c98e-11eb-8fb9-e796cc884156.png)

```git
git remote add upstream https://github.com/azerothcore/azerothcore-wotlk
```

**Origin**, para un colaborador, siempre es el repositorio que él puede modificar, en cambio **upstream**, es de quien descarga los cambios y actualiza. Porque algo importante, es que el emulador, debe estar siempre lo más actualizado posible. De esa forma, yo puedo realizar un **git push** a origin, pero no podría hacerlo nunca a **upstream** porque ese repositorio no me pertenece. Si bien, estamos un poco mezclando los 2 artículos, el de crear un PR y el de testear un PR, es importante que se entienda la diferencia entre solo tester y tester y colaborar.

Ahora, lo que necesitamos hacer, es posicionarnos siempre en la rama **master** y crear una nueva rama, para poder descargar los cambios del pull request que queremos probar. Por ejemplo, vamos a tomar como referencia el siguiente pull request: [PR 5949](https://github.com/azerothcore/azerothcore-wotlk/pull/5949){:target="_blank"}. De la URL del PR, obtenemos el id, en este caso el **5949**

- Nos aseguramos de estar en master
```git
git checkout master
```
- Verificamos de tener todo actualizado siempre
```git
git pull upstream master
```
- Creamos una rama nueva, por convención
```git
git checkout -b pr-5949
```
- Descargamos los cambios del PR a esa rama
```git
git pull upstream pull/5949/head
```

**Nota:** si no tienen upstream, porque no son colaboradores, utilicen origin en su lugar. En la documentación de AzerothCore, utilizan ese método, la idea de este artículo, es mostrar ambos puntos al mismo tiempo, el de colaborador y el de tester.

En el caso, de que el PR agregue o elimine archivos, se debe utilizar el CMAKE para que la solución de visual studio o la compilación en Linux, reconozca esos archivos que se agregaron o se eliminaron. Si no ocurre eso, solamente deberíamos de compilar el emulador, y verificar los temas que se suelen detallar en el pull request. También siempre es bueno, adjuntar alguna imagen (se puede arrastrar hasta la caja de texto, y en unos pocos segundos se sube).

De mas esta decirles, que si llegaron hasta este punto y tienen dudas, pueden hacerme consultas por discord, siempre estoy dispuesto a ayudar a las personas que quieran ser testers o contribuidores de AzerothCore y que por algún motivo, no se animen a dar el primer paso. Pueden escribir en el chat, o incluso nombrarme, o enviarme un mensaje privado. Siempre está dispuesto a ayudar a aquellos que quieran colaborar.

En la wiki de AzerothCore, tienen otros ejemplos y también un poco más de documentación, por lo que les dejo el enlace para que lo lean.

Fuente: [Articulo original de la wiki de AzerothCore](https://www.azerothcore.org/wiki/How-to-test-a-PR){:target="_blank"}
