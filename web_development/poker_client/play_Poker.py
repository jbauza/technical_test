import time
from classes import PokerGame
from utils import highCard, hasOnePair, hasTwoPairs, hasThreeOfAKind

print "Comencemos el juego!"
print "--------------------"

poker = PokerGame()

while poker.isLive():
    print '\n', "cartas restantes en baraja: ", poker.deck_size 
    opcion = raw_input("Que desea hacer?(<jugar>, <mezclar> o <salir>): ")

    if opcion == 'salir':
        time.sleep(1)
        print "ok, adios!"
        poker.endGame()
        break

    elif opcion == 'mezclar':
        poker.shuffleDeck()
        continue

    elif opcion == "jugar":
        
        print '\n',"jugador 1 pide cartas:"
        hand1 = poker.getHand()
        if hand1.cards:
            time.sleep(1)
            print 'cartas:', hand1
            print hand1.getMapNumber().values()
        else:
            continue
        
        time.sleep(2)

        print '\n',"jugador 2 pide cartas:"
        hand2 = poker.getHand()
        if hand2.cards:
            time.sleep(1)
            print 'cartas:', hand2
            print hand2.getMapNumber().values()
        else:
            print "No quedan suficientes cartas, se debe volver a revolver la baraja."
            continue

        print "--------------------"

    else:
        continue
