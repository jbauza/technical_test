import requests
import json

DECK = {
    'A' : 13,
    '2' : 1,
    '3' : 2,
    '4' : 3,
    '5' : 4,
    '6' : 5,
    '7' : 6,
    '8' : 7,
    '9' : 8,
    '10' : 9,
    'J' : 10,
    'Q' : 11,
    'K' : 12,
}

gameRank = {
    10 : 'Royal Flush', 
    9 : 'Straight Flush', 
    8 : 'Four of a Kind', 
    7 : 'Full House', 
    6 : 'Flush', 
    5 : 'Straight', 
    4 : 'Three of a Kind', 
    3 : 'Two Pairs', 
    2 : 'One Pair', 
    1 : 'High Card', 
}

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

    def chooseWinner(self, game1, game2):
        if game1[0] == game2[0]:
            return False
        elif game1[0] > game2[0]:
            return game1
        else:
            return game2

    def highCardFromList(self,cards):
        cards_numbers = [card.number for card in cards]
        cards_values = [DECK[c] for c in cards_numbers]
        max_val = max(cards_values)
        i_val = cards_values.index(max_val)
        max_card = cards[i_val]
        
        return max_card

    def tieBreaker(self, cards1, cards2):

        if len(cards1) == 0 and len(cards2) == 0:
            return False

        high_card1 = self.highCardFromList(cards1)
        high_card2 = self.highCardFromList(cards2)
        card1_value = DECK[high_card1.number]
        card2_value = DECK[high_card2.number]

        if card1_value > card2_value:
            return (1, high_card1)
        elif card1_value < card2_value:
            return (2, high_card2)
        else:
            cards1.remove(high_card1) 
            cards2.remove(high_card2) 
            return self.tieBreaker(cards1, cards2)

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

    def highCard(self):
        cards_numbers = [card.number for card in self.cards]
        cards_values = [DECK[c] for c in cards_numbers]
        max_val = max(cards_values)
        i_val = cards_values.index(max_val)
        max_card = self.cards[i_val]
        
        return max_card

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
    
    def hasOnePair(self):
        if self.hasAnyPair():
            val_cards = [c.number for c in self.cards]
            cards = list(set(val_cards))
            if len(cards) == 4:
                seen = []
                pair_card_number = 0 
                for c in val_cards:
                    if c in seen:
                        pair_card_number = c
                        break
                    else:
                        seen.append(c) 
                pair = self.getNumber(pair_card_number)
         
                return pair
        return False

    def hasTwoPairs(self):
        if self.hasAnyPair():
            val_cards = [c.number for c in self.cards]
            cards = list(set(val_cards))
            if len(cards) == 3:
                seen = {}
                three_card_number = 0 
                for c in val_cards:
                    if c in seen:
                        seen[c] += 1
                    else:
                        seen[c] = 1
                if 2 in seen.values(): 
                    pairs = []
                    for c in cards:
                        if seen[c] == 2:
                            pair = self.getNumber(c)
                            pairs.append(pair)
                    return pairs
        return False

    def hasThreeOfAKind(self):
        if self.hasAnyThreeOfKind() and not self.hasAnyPair():
            cards_map = self.getMapNumber()
            i_number = cards_map.values().index(3)
            number = cards_map.keys()[i_number]
            return self.getNumber(number)

        return False

    def hasStraight(self):
        cards_number = [c.number for c in self.cards]
        diff_cards = list(set(cards_number))
        if len(diff_cards) == 5:
            cards_values = [DECK[n] for n in cards_number]
            #caso de dar vuelta la baraja
            if 12 in cards_values and 1 in cards_values:
                if 13 not in cards_values:
                    return False
                else:
                    union_cards = [12,13,1]
                    other_cards = list(set(cards_values)-set(union_cards))
                    
                    if 11 not in other_cards:
                        if 2 in other_cards and 3 in other_cards:
                            return self.cards
                    elif 2 not in other_cards:
                        if 11 in other_cards and 10 in other_cards:
                            return self.cards
                    elif 11 in other_cards and 2 in other_cards:
                        return self.cards
                    else:
                        return False

            else:
                cards_values.sort()
                ace = False
                if 13 in cards_values:
                    ace = True
                    cards_values = cards_values[0:-1]

                before = None
                for v in cards_values:
                    #first item
                    if before is None:
                        before = v
                    else:
                        if v == before+1:
                            before = v
                        else:
                            return False
                if ace:
                    if 1 not in cards_values and 12 not in cards_values:
                        return False

                return self.cards

        return False

    def hasFlush(self):
        suit = self.cards[0].suit
        cards_with_suit = self.getSuit(suit)
        if len(cards_with_suit) == len(self.cards):
            return self.cards

        return False

    def hasFullHouse(self):
        if self.hasAnyThreeOfKind() and self.hasAnyPair():
            return self.cards
        else:
            return False

    def hasFourOfAKind(self):
        cards_map = self.getMapNumber()
        if 4 in cards_map.values():
            i_number = cards_map.values().index(4)
            number = cards_map.keys()[i_number]
            return self.getNumber(number)
            
        return False

    def hasStraightFlush(self):
        if self.hasFlush() and self.hasStraight():
            return self.cards

        return False

    def hasRoyalFlush(self):
        if self.hasStraightFlush():
            royal_numbers = ['10','J','Q','K','A']
            cards_number = [c.number for c in self.cards] 
            for rn in royal_numbers:
                if rn not in cards_number:
                    return False

            return self.cards
           
        return False

    def getBestGame(self):
        if self.hasRoyalFlush():
            return (10, gameRank.get(10), self.hasRoyalFlush())
        elif self.hasStraightFlush():
            return (9, gameRank.get(9), self.hasStraightFlush())
        elif self.hasFourOfAKind():
            return (8, gameRank.get(8), self.hasFourOfAKind())
        elif self.hasFullHouse():
            return (7, gameRank.get(7), self.hasFullHouse())
        elif self.hasFlush():
            return (6, gameRank.get(6), self.hasFlush())
        elif self.hasStraight():
            return (5, gameRank.get(5), self.hasStraight())
        elif self.hasThreeOfAKind():
            return (4, gameRank.get(4), self.hasThreeOfAKind())
        elif self.hasTwoPairs():
            return (3, gameRank.get(3), self.hasTwoPairs())
        elif self.hasOnePair():
            return (2, gameRank.get(2), self.hasOnePair())
        else:
            #High Card
            return (1, gameRank.get(1), [self.highCard()])

    def __repr__(self):
        return '['+','.join([c.__str__() for c in self.cards])+']'
