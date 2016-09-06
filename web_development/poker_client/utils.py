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
        pair = hand.getNumber(pair_card_number)
 
        return pair

    return False

def hasTwoPairs(hand):
    val_cards = [c.number for c in hand.cards]
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
                    pair = hand.getNumber(c)
                    pairs.append(pair)
            return pairs
        
    return False

def hasThreeOfAKind(hand):
    val_cards = [c.number for c in hand.cards]
    cards = list(set(val_cards))
    if len(cards) == 3:
        seen = {}
        three_card_number = 0 
        for c in val_cards:
            if c in seen:
                seen[c] += 1
            else:
                seen[c] = 1
        if 3 in seen.values(): 
            three = hand.getNumber(seen.keys()[seen.values().index(3)])
            return three
        
    return False

def isFourOfAKind(hand):
    return False

def hasFlush(hand):
    suit = hand.cards[0].suit
    cards_with_suit = hand.getSuit(suit)
    if len(cards_with_suit) == len(hand.cards):
        return hand.cards

    return False

def hasRoyalFlush(hand):
    if hasFlush(hand):
        royal_numbers = ['10','J','Q','K','A']
        cards_number = [c.number for c in hand.cards] 
        for rn in royal_numbers:
            if rn not in cards_numbers:
                return False

        return hand.cards
       
    return False

def hasStraightFlush(hand):
    if hasFlush(hand):
        cards_number = [c.number for c in hand.cards]
        diff_cards = list(set(cards_number))
        if len(diff_cards) == 5:
            cards_values = [DECK[n] for n in cards_number]
            cards_values.sort()
            before = None
            for v in cards_values:
                #check ace
                if before == 13:
                    before = 0 
                #first item
                if before is None:
                    before = v
                else:
                    if v == before+1:
                        before = v
                    else:
                        return false

            return hand.cards
            
    return False

