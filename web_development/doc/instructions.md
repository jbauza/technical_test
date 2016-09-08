# Resumen
El sistema consiste en un cliente Python que se conecta al dealer http://dealer.internal.comparaonline.com:8080/ para pedir manos de cartas y evaluarlas con las reglas del Poker a través de un prompt interactivo con un usuario por la consola de comandos.

El sistema esta constituido por 2 scripts python:

## classes.py: 
Este script contiene todos los objetos y metodos necesarios para la implementación del juego y se listan a continuación:
* PokerGame : Maneja la conexion al dealer, pide manos y contiene reglas generales para dirimir el ganador del juego.
* Card: Objeto basico que contiene un valor(*number*) y una pinta(*suit*)
* Hand: Contiene la lista que componen la *mano de cartas* y todos los metodos necesarios para evaluar las reglas de poker. Por defecto se manejan *manos* de 5 cartas.

## play_Poker.py

Este script es el juego y contiene la logica del juego (Pedir 2 manos de cartas y evaluar al ganador), donde el usuario tiene 2 opciones posibles:
* *jugar*: Pedir 2 manos de cartas y mostrar el resultado de cual es la mano ganadora. Esta acción se puede realizar hasta que el *token* expire o se agoten las cartas del mazo, donde el usuario esta obligado a mezclar para continuar.
* *mezclar*: Pide un nuevo *token* al dealer lo cual simula una mezcla de las cartas, dejando 52 disponibles.
* *salir*: Sale del prompt interactivo.

# Forma de uso

Para utilizar el juego se debe ejecutar el siguiente comando:
```
\>python play_Poker.py 
```
Lo cual da inicio al juego:
```
Comencemos el juego!
--------------------
El dealer esta barajando

cartas restantes en baraja:  52
Que desea hacer?(<jugar>, <mezclar> o <salir>):
```
En este prompt, el usuario debe escribir cual de las 3 opciones desea ejecutar(*jugar*,*mezclar* o *salir*). En caso de escribir otra cosa, el prompt vuelve a pedir el ingreso de las acciones mencionadas.

# Ejemplo de uso
```
Comencemos el juego!
--------------------

cartas restantes en baraja:  52
Que desea hacer?(<jugar>, <mezclar> o <salir>): jugar
---------

jugador 1 pide cartas:
El dealer esta preparandose para repartir
cartas:  [2 spades,4 diamonds,A clubs,K diamonds,A diamonds]
---------
juego:  One Pair [A clubs, A diamonds]
---------

jugador 2 pide cartas:
cartas: [8 diamonds,4 clubs,J spades,3 diamonds,Q diamonds]
---------
juego:  High Card [Q diamonds]
---------

El ganador es:

jugador 1!!!!!
con:  One Pair [A clubs, A diamonds]
--------------------
--------------------

cartas restantes en baraja:  42
Que desea hacer?(<jugar>, <mezclar> o <salir>): mezclar
El dealer esta barajando

cartas restantes en baraja:  52
Que desea hacer?(<jugar>, <mezclar> o <salir>): salir

ok, adios!
```
