import time
from classes import PokerGame

print "Comencemos el juego!"
print "--------------------"

poker = PokerGame()

while poker.isLive():
    print '\n', "cartas restantes en baraja: ", poker.deck_size 
    opcion = raw_input("Que desea hacer?(<jugar>, <mezclar> o <salir>): ")

    if opcion == 'salir':
        print '\n',"ok, adios!"
        poker.endGame()
        break

    elif opcion == 'mezclar':
        poker.shuffleDeck()
        continue

    elif opcion == "jugar":
        
        print "---------"
        print '\n',"jugador 1 pide cartas:"
        hand1 = poker.getHand()
        if hand1.cards:
            print 'cartas: ', hand1
            time.sleep(1)
            game1 = hand1.getBestGame()
            #nombre y cartas de la mano del resultado
            print "---------"
            print 'juego: ', game1[1], game1[2]
        else:
            continue
        
        print "---------"
        time.sleep(2)

        print '\n',"jugador 2 pide cartas:"
        hand2 = poker.getHand()
        if hand2.cards:
            print 'cartas:', hand2
            time.sleep(1)
            game2 = hand2.getBestGame()
            #nombre y cartas de la mano del resultado
            print "---------"
            print 'juego: ', game2[1], game2[2]
        else:
            continue

        print "---------"
        time.sleep(1)
        print '\n',"El ganador es:",'\n'
        time.sleep(1)

        winner = poker.chooseWinner(game1, game2)
        if winner:
            if winner == game1:
                print "jugador 1!!!!!"
            else:
                print "jugador 2!!!!!"
            print "con: ", winner[1], winner[2]
        else:
            print "Empate de: ", game1[1], "!!!!"
            time.sleep(1)
            print "Se decidira por carta mas alta"
            winner = poker.tieBreaker(hand1.cards, hand2.cards)
            time.sleep(1)
            print '\n',"El ganador es:"
            time.sleep(1)
            if winner:
                if winner[0] == 1:
                    print "jugador 1!!!!!"
                else:
                    print "jugador 2!!!!!"
                print "con la carta mas alta: ", winner[1]

            else:
                print "Empate!, ambos jugadores tienen la misma mano. Increible!"

        print "--------------------"
        print "--------------------"

    else:
        continue
