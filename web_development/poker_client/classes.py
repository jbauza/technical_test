class Session(object):
    base_url = '' 
    token_url = ''
    
    def __init__(self):
        self.token = None

    def beginGame(self):
        self.token = 1 

    def getCards(self, number):
        return number

class Card(object):

    def __init__(self, number, suit):
        self.number = number
        self.suit = suit

    def __repr__(self):
        return self.number+' '+self.suit
    
    def __str__(self):
        return self.number+' '+self.suit
