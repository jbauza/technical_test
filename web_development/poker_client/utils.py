from classes import Card, Hand

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

def checkHand(hand):
    result
    return result

def highCard(hand):
    cards_numbers = [card.number for card in hand.cards]
    cards_values = [DECK[c] for c in cards_numbers]
    max_val = max(cards_values)
    i_val = cards_values.index(max_val)
    max_card = hand.cards[i_val]
    
    return max_card

def hasOnePair(hand):
    
    val_cards = [c.number for c in hand.cards]
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
        par = hand.getNumber(pair_card_number)
        print par
 
        return True
    else:
        return False

def isRoyalFlush(hand):

    return True

def isStraightFlush(hand):

    return True

def isFourOfAKind(hand):
    return False
