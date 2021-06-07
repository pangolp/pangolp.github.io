title: mod-recruit-friend
description: Con este módulo, podrás reclutar un amigo ingame a través de un comando, y obtener todos los beneficios blizzlike del emulador. Compatible con el emulador de AzerothCore, pero quizás pueda ser adaptado para otros emuladores. También tiene un comando de reset sin costo alguno.
authors: Pagani Walter
date: 2021.06.07
summary: La mejor opción para reclutar un amigo ingame.
category: Módulos
tags: azerothcore, server335, mod-recruit-friend
repository: https://github.com/pangolp/mod-recruit-friend

[![mod-recruit-friend](https://user-images.githubusercontent.com/2810187/83866937-ef9a6b00-a6fe-11ea-9fd7-4cb3c0465bba.png)](https://www.youtube.com/watch?v=ko1F_fIbnJg "mod-recruit-friend")

# Modulo: Reclutar un amigo.

## ¿Para qué es el módulo?

El módulo permite a los jugadores reclutar a un amigo dentro del juego y obtener los beneficios del mismo.

- Experiencia de misión mejorada
- Mejora de la experiencia mediante la eliminación del npc
- Dale un nivel a un amigo, por cada nivel obtenido.
- Invoca a un amigo, una vez cada 60 minutos.

Los comandos que se pueden utilizar son:

```
.recruit add nombre_del_jugador_a_reclutar
.recruit reset
```

**Nota:** Debes ingresar el nombre de tu compañero. Una vez ejecutado con éxito, aparecerá un mensaje en el chat, pidiéndote que desloguees y que vuelvas a ingresar. Es importante que salgas por completo del juego, no basta con salir del personaje, debes cerrar la cuenta y volver a abrirla. Dado que se modifica un valor dentro de la base de datos `auth.account` y la misma debe ser leída nuevamente.

El comando reset, también te pedirá que salgas y vuelvas a ingresar, porque lo que hace, es simplemente resetear el valor y agregarle un 0, donde antes estaba el `account.id` de tu compañero. De esa forma, podrás volver a reclutar a otro amigo si es que el mismo no puede continuar jugando.

Espero que te sirva y puedas disfrutarlo.
