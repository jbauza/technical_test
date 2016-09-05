import sys
import json
import time
import requests
from classes import Card

base_url = 'http://dealer.internal.comparaonline.com:8080/'

token_url = base_url + 'deck'
response = requests.post(token_url)

if response.status_code != 200:
    sys.exit(0)

token = response.text
print 'token', token

num_cards = 5
get_cards_url = base_url + '/'.join(['deck',token,'deal',str(num_cards)])
print get_cards_url

for i in range(1,18):
    time.sleep(70)
    
    get_cards = requests.get(get_cards_url)

    if get_cards.status_code == 200:
        cards_hand = json.loads(get_cards.text)
        this_hand = []
        for card in cards_hand:
            this_hand.append(Card(card["number"], card["suit"]))

        print this_hand
    elif get_cards.status_code == 405:
        print "sin cartas"
    else:
        print get_cards.status_code
