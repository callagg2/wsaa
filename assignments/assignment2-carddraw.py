# Assignment: Deal cards
# Author: Gerry Callaghan
# Date: 04-02-2026

import requests
import csv

# Pick a desk of cards
URL= "https://deckofcardsapi.com/api/deck/new/"
response=requests.get(URL)
data = response.json()
#print(data)

#Shuffle the cards
URL2= f"https://deckofcardsapi.com/api/deck/{data['deck_id']}/shuffle/?deck_count=1"
response=requests.get(URL2)
data2 = response.json()
#print(data2)

# Pick 5 cards from the deck
URL3= f"https://deckofcardsapi.com/api/deck/{data['deck_id']}/draw/?count=5"
response=requests.get(URL3)
data3 = response.json()
#print(data3)
print (f"The first card is:\t{data3['cards'][0]['value']} of {data3['cards'][0]['suit']}")
print (f"The second card is:\t{data3['cards'][1]['value']} of {data3['cards'][1]['suit']}")
print (f"The third card is:\t{data3['cards'][2]['value']} of {data3['cards'][2]['suit']}")
print (f"The fourth card is:\t{data3['cards'][3]['value']} of {data3['cards'][3]['suit']}")
print (f"The fifth card is:\t{data3['cards'][4]['value']} of {data3['cards'][4]['suit']}")

'''
# Check if the user has drawn a pair, triple, straight, or all of the same suit and congratulate the user.

Need to work more on this - NOT finished

for card in data3['cards']:
    if card['value'] == 'ACE':
        card['value'] = 1
    elif card['value'] == 'JACK':
        card['value'] = 11
    elif card['value'] == 'QUEEN':
        card['value'] = 12
    elif card['value'] == 'KING':
        card['value'] = 13
    else: # for all the non-face cards, convert the value to an integer
        card['value'] = int(card['value'])
#assign values to each of the cards
values = card['value'] 

for card in data3['cards']:
    #assign suits to each of the cards
    suits = card['suit']
    if len(set(suits)) == 1:
        print("Congratulations! You have drawn all cards of the same suit!")
    elif len(set(values)) == 1:
        print("Congratulations! You have drawn a pair!")
    elif len(set(values)) == 2:
        print("Congratulations! You have drawn a triple!")
    elif sorted(values) == list(range(min(values), max(values)+1)):
        print("Congratulations! You have drawn a straight!")
    else:
        print("Better luck next time! You did not draw a pair, triple, straight, or all of the same suit.")
'''








