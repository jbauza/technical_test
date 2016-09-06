from classes import PokerGame
from utils import highCard, hasOnePair, hasTwoPairs, hasThreeOfAKind

print "Comencemos el juego!"
#print """Instrucciones:
#Presiona 1 para para pedir una mano
#Presiona 2 para revolver la baraja
#Presiona 3 para terminar
#"""

poker = PokerGame()


hand1 = poker.getHand()
print 'p1', hand1
print hasTwoPairs(hand1)

hand2 = poker.getHand()
print 'p2', hand2
print hasTwoPairs(hand2)

print poker.deck_size

poker.shuffleDeck()
print poker.token
print poker.deck_size
