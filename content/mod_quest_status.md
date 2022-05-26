title: mod-quest-status
description: Con este módulo, como GM, vas a poder tener una mejor información sobre las cadenas largas de misiones, y de esa forma, poder ayudar a la gente, cuando no sepa donde se quedó. Te permite crear macros mucho más chico, con cadenas grandes de misiones.
authors: Pagani Walter
date: 2022.05.26
summary: Con este módulo, como GM, vas a poder tener una mejor información sobre las cadenas largas de misiones, y de esa forma, poder ayudar a la gente, cuando no sepa donde se quedó. Te permite crear macros mucho más chico, con cadenas grandes de misiones.
category: Módulos
tags: azerothcore, server335, mod-quest-status
repository: https://github.com/pangolp/mod-quest-status

# mod-quest-status

Cuando empecé con el tema del desarrollo, lo cual primero o en forma paralela, fui GM de un servidor. Me di cuenta, que muchas veces las personas abandonan misiones, porque se les hacen muy pesadas, o de repente, obtienen el nivel máximo y creen que esa cadena que estaban haciendo, ya no la necesitan más. En el caso de la 3.3.5ª, existen muchos ejemplos. Los cuales vamos a detallar a continuación.

- Caballeros de la Espada de Ébano
- Cruzada Argenta
- El Acuerdo del Reposo del Dragón
- El Kirin Tor
- Los Hijos de Hodir

La mayoría de las facciones que nombre anteriormente, suelen tener varias misiones, repartidas por diferentes mapas. Mientras uno va subiendo de nivel, se va cruzando con misiones que le dan reputación con estas facciones. Pero cuando puede cruzarse a otro mapa o puede abandonar las misiones, generalmente lo hace. Y luego, cuando quiere retomarlas, no sabe en qué parte de la cadena se quedó. Es por eso que pregunte, ¿Cómo podíamos obtener información sobre el estado que tenía una misión? En otras palabras, saber si el jugador la había hecho o no. Y me hablaron del comando **lookup quest**.

El comando por defecto, necesita como parámetro, es decir, luego de usar el comando, el nombre de la misión que queremos buscar. Y luego, podemos seleccionar a la persona, y saber si la completo o no, y en qué estado se encuentra la misma. Pero tenemos varios problemas con esto. **Primero** muchas misiones tienen el mismo nombre. **Segundo** tenemos que poner el nombre en inglés. **Y tercero**, el macro, que sería la forma más cómoda para poder usarlo, tiene un límite de 255 caracteres si no recuerdo mal.

Dejo unas imágenes sobre el comando en la actualidad y del macro.

![macro](https://user-images.githubusercontent.com/2810187/170588896-79345b8f-18b9-41ad-a308-274fa59336a6.png)

![chat](https://user-images.githubusercontent.com/2810187/170588906-1967b636-1f87-4333-9e26-ba32bc488a9a.png)

El macro original ocupa **105 caracteres de un máximo de 255**. Y claramente, solamente tengo 3 misiones. Pero a su vez, como se puede observar en el chat, cuando se usa. La primera misión esta 2 veces, porque existe una misión para la alianza y otra para la hora con el mismo nombre. Además, de que tenemos que ponerle el nombre en inglés. Y si bien, el título de la quest, puede ser más corto, eso podría hacer que traiga otras misiones, que realmente no tienen nada que ver con la cadena, y podemos llegar a confundirnos nosotros o confundir a la persona que estamos intentando ayudar.

Ahora dejo fotos, de un macro con el comando que me da el modulo.

![comando_qs](https://user-images.githubusercontent.com/2810187/170588907-765af488-07f1-43df-8f00-e5d67724235e.png)

![comando_qs_chat](https://user-images.githubusercontent.com/2810187/170588909-0c8f29a3-25ee-4658-8c80-8a39161dd240.png)

La misma función, por así decirlo, ahora ocupa **39 de 255 caracteres disponibles**, lo que hace que sea mucho más corto, por más que añada una quest mas, no superó los 50 caracteres. Eso me permite, poner muchas más misiones de las quest podría de la otra forma. Y a su vez, gano precisión, porque ahora tengo los IDS, entonces, puedo hacer un macro por facción, y de esa forma, tener una mejor respuesta, lo que hace que pueda asesorar mejor a la persona que está perdida.

**Conclusión:** Si se limita un poco el uso del macro, se podría establecer, para que el mismo jugador, pueda auto inspeccionarse, sin la ayuda de un maestro de juego, pero para eso, habría que limitar la cantidad de consultas, porque si varias personas se ponen a spamear el comando, podrían saturar el servidor. Haciendo que solamente realice una cierta cantidad de consultas por hora, se podría habilitar para todo el mundo.
