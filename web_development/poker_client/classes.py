import requests
import json

class PokerGame(object):
    BASE_URL = 'http://dealer.internal.comparaonline.com:8080/'
    TOKEN_URL = BASE_URL + 'deck'
    deck_size = 0 
    token = None
    
    def __init__(self):
        self.shuffleDeck()

    def shuffleDeck(self):
        response = requests.post(self.TOKEN_URL)
        
        if response.status_code == 200:
            self.deck_size = 52
            self.token = response.text
        elif response.status_code == 500:
            print "El dealer no esta disponible"
        else:
            print "Ocurrio un error HTTP con estado", response.status_code

    #Por defecto se pide una mano de 5 cartas
    def getHand(self, number=5):

        if self.token is None:
            print "No hay dealer disponible"
            return None


        hand = Hand()
        cards_url = self.BASE_URL + '/'.join(['deck', self.token, 'deal', str(number)]) 
        get_hand = requests.get(cards_url)

        if get_hand.status_code == 200:
            self.deck_size -= number
            json_hand = json.loads(get_hand.text)
            for jcard in json_hand:
               hand.append(Card(jcard["number"], jcard["suit"])) 

        elif get_hand.status_code == 405:
            print "No quedan suficientes cartas en la baraja, solo quedan ", self.deck_size

        elif get_hand.status_code == 404:
            print "", 405

        else:
            print "Error HTTP", get_hand.status_code

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
            if c.number == suit:
                has_suit.append(c)

        return has_suit  

    
    def __repr__(self):
        return '['+','.join([c.__str__() for c in self.cards])+']'
