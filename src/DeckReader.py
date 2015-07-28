# Deck Reader

## Reads the lines of flashcard data and converts them into a deck

import Card

def create_deck(file_data):
    ''' Creates a deck by creating cards with clues and answers from
        supplied file data.
    '''

    deck = []

    for line in file_data:
        line            = line.decode().strip()
        clue, answers   = line.split(';')
        
        clue            = clue.strip()
        answers         = answers.strip().upper().split(',')
        answers         = [answer.strip() for answer in answers]

        card            = Card.Card(clue, answers)
        deck.append(card)

    return deck
