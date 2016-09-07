import requests
import json

class PokerGame(object):
    BASE_URL = 'http://dealer.internal.comparaonline.com:8080/'
    TOKEN_URL = BASE_URL + 'deck'
    deck_size = 0 
    token = None
    
    def __init__(self):
        self.shuffleDeck()

    def responseOk(self, response):
        #HTTP code 200
        if response.status_code == requests.codes.ok:
            return True
        else:
            return False

    def isLive(self):
        return True if self.token is not None else False
     
    def endGame(self):
        self.token = None
        self.deck_size = 0

    def shuffleDeck(self):
        response = requests.post(self.TOKEN_URL)
        
        if self.responseOk(response):
            self.deck_size = 52
            self.token = response.text

        elif response.status_code == 500:
            print "El dealer esta barajando"
            #retry if HTTP code 500
            self.shuffleDeck()
        else:
            print "Ocurrio un error HTTP con estado", response.status_code
            self.endGame()

    #Por defecto se pide una mano de 5 cartas
    def getHand(self, number=5):

        if not self.isLive():
            print "No hay dealer disponible"
            return None

        hand = Hand()
        cards_url = self.BASE_URL + '/'.join(['deck', self.token, 'deal', str(number)]) 
        get_hand = requests.get(cards_url)

        if self.responseOk(get_hand):
            self.deck_size -= number
            json_hand = json.loads(get_hand.text)
            for jcard in json_hand:
               hand.append(Card(jcard["number"], jcard["suit"])) 

        elif get_hand.status_code == 500:
            #Si falla pide nuevamente una mano
            print "El dealer esta preparandose para repartir"
            return self.getHand()
            
        elif get_hand.status_code == 405:
            print "No quedan suficientes cartas en la baraja, solo quedan ", self.deck_size
            print "Se debe volver a revolver!"

        elif get_hand.status_code == 404:
            print "El dealer ha dejado el juego."
            self.endGame()
            return False

        else:
            print "Error HTTP", get_hand.status_code
            self.endGame()
            return False

        return hand

    def __repr__(self):
        if self.token is None:
            return "No hay dealer disponible"
        else:
            return "El dealer esta barajando..."

class Card(object):

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __repr__(self):
        return self.number+' '+self.suit
    
    def __str__(self):
        return self.number+' '+self.suit

class Hand(object):

    def __init__(self):
        self.cards = []

    def append(self, card):
        self.cards.append(card)

    def getNumber(self, number):
        has_number = []
        for c in self.cards:
            if c.number == number:
                has_number.append(c)

        return has_number

    def getSuit(self, suit):
        has_suit = []
        for c in self.cards:
            if c.suit == suit:
                has_suit.append(c)

        return has_suit  

    def getMapNumber(self):
        map_number = {}
        for c in self.cards:
            if c.number in map_number:
                map_number[c.number] += 1
            else:
                map_number[c.number] = 1 

        return map_number

    def hasAnyPair(self):
        cards_map = self.getMapNumber()
        if 2 in cards_map.values():
            return True
        else:
            return False

    def hasAnyThreeOfKind(self):
        cards_map = self.getMapNumber()
        if 3 in cards_map.values():
            return True
        else:
            return False
    


    def __repr__(self):
        return '['+','.join([c.__str__() for c in self.cards])+']'
