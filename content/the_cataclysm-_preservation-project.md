title: The Cataclysm Preservation Project
description: En esta ocasión, les cuento mi experiencia compilando el emulador público de Cataclismo.
date: 2022.05.25
authors: Pagani Walter
summary: Una interesante alternativa, si te interesa el open source, y queres trabajar en la expansión.
category: Emuladores
tags: trinitycore, emuladores, cataclismo
repository: https://github.com/The-Cataclysm-Preservation-Project/

![cata](https://images7.alphacoders.com/335/335570.jpg)

# The Cataclysm Preservation Project

![WoWScrnShot_052522_071920](https://user-images.githubusercontent.com/2810187/170356891-c4094035-7bf8-45c8-b72f-f80ae66e0127.jpg)

Hola, buenas tardes. No es la primera vez que realmente trabajo con un source de cataclismo, pero si es cierto, que es la primera vez que lo hago con un código fuente público. Si bien el repositorio lo conozco hace mucho tiempo, no había tenido posibilidad de probarlo. Porque cuando quise hacerlo, AzerothCore, todavía usaba ACE y no tenía boots, por lo que yo no tenía instala la dependencia, y en Linux, pedía por aquel entonces, una dependencia que no estaba disponible para la versión que yo usaba, y realmente antes no era de compilar librerías. Siempre fiel al `apt install`.

Mi intención era probar, si podía compilar el emulador, descargando el código fuente primero en Windows y luego por supuesto hacer lo propio en Linux. En Windows de momento, no he tenido problemas. Clone el repositorio, utilice el cmake para crear la solución, abrí el visual studio y luego de un par de minutos, no recuerdo bien cuantos, tenía los ejecutables, junto con los extractores. **Nota:** hago hincapié en el tema de los extractores, porque muchas veces los repositorios públicos y privados que están publicados, no mantiene el código de las librerías, solamente hacen scripts y modificaciones SQL, del resto no tocan nada.

Luego venia la incógnita de donde iba a conseguir un cliente blizzlike, sin ningún tipo de parche o modificación. Porque realmente quería extraer todo la información, de la manera más limpia posible. Termine haciendo la extracción de un cliente que tenia de un servidor, pero observe bastantes mensajes de errores y de otros tipos, por lo que en un futuro, intentare volver a extraerlos, luego cuando se termine de descargar el nuevo cliente.

### Cliente

Respecto al cliente, tenemos que tener en cuenta, que no nos sirven los clientes que hayamos usado anteriormente, porque este repositorio utiliza bnet, y entonces ese sistema, requiere parchear el cliente oficial, como lo explican en la siguiente guía en inglés: [guía]( https://github.com/The-Cataclysm-Preservation-Project/TrinityCore/wiki/Setup-and-troubleshooting-for-connecting). Mi consejo es, leer bien la guía, porque en un momento, posiblemente por las ganas de verlo funcionando, me saltie un paso, y varias veces tuve que reconstruir todo el tema del cliente, porque se dañan los archivos, así que leerlo con tranquilidad.

### Dentro del juego.

![WoWScrnShot_052522_064824](https://user-images.githubusercontent.com/2810187/170356802-e32dba9e-8b9c-4e3b-9670-84c7be18a611.jpg)

Una vez logre tener el servidor funcionando y poder hacer ingresar, me cree un druida wargen porque lo que siempre queremos ver, son las zonas de inicio de las razas nuevas, dado que quizás es parte del contenido que a la enorme mayoría que no jugamos la expansión, nos pueda llamar la atención. Así que me dispuse a hacer misiones, encontré que faltan muchas traducciones al español (aunque eso es normal) pero no me encontré ningún bug de momento, en lo que yo llevo jugando (aclaro que no termine de hacer todas las misiones)

Espero que los que les comente en este post, les sirva, y si es necesario, armaremos otros post, o incluso, intentamos hacer algún video en el canal, donde compilaremos el emulador y veremos algunas cosas (sin entrar en detalles en los derecho de autor, que son las cosas que la comunidad no comparte, y por supuesto que yo tampoco puedo hacerlo) para evitar problemas. Recuerden que todos los videos, son de carácter educativos. Dado que no tengo un servidor, ni trabajo para ninguno de los que se encuentran en línea en este momento.
