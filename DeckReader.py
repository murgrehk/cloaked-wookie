#Deck Reader
## Reads the lines in a flashcard file and converts it into a deck

import Card

def createDeck(file_name):
    deck = []
    num_cards = 0

    with open(file_name) as f:
        for line in f:
            line = line.strip()
            pair = line.split(';')
            
            if pair == line: #no semicolon
                card = None           
            else:
                clue = pair[0].strip()
                answers = pair[1].strip().upper().split(',')
                answers = [element.strip() for element in answers]
                card = Card.Card(clue, answers)
                
            deck.append(card)

    return deck
