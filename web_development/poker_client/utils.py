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
    if hand.hasAnyPair():
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
    if hand.hasAnyPair():
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

def hasStraight(hand):
    cards_number = [c.number for c in hand.cards]
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
                        return hand.cards
                elif 2 not in other_cards:
                    if 11 in other_cards and 10 in other_cards:
                        return hand.cards
                elif 11 in other_cards and 2 in other_cards:
                    return hand.cards
                else:
                    return False

        else:
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
                        return False

        return hand.cards

    return False

def hasFlush(hand):
    suit = hand.cards[0].suit
    cards_with_suit = hand.getSuit(suit)
    if len(cards_with_suit) == len(hand.cards):
        return hand.cards

    return False

def hasFullHouse(hand):
    if hand.hasAnyThreeOfKind() and hand.hasAnyPair():
        return hand.cards
    else:
        return False

def hasFourOfAKind(hand):
    cards_map = hand.getMapNumber()
    if 4 in cards_map.values():
        #falta mostrar los 4 repetidos
        return hand.cards
        
    return False

def hasStraightFlush(hand):
    if hasFlush(hand) and hasStraight(hand):
        return hand.cards
    else: 
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

