# Flashcard Viewer

## Author: Seth Ebner
## Created 8-14-14
## Modified: 8-16-14

import random
import DeckReader
import TabulateResults
import pickle
import sys

def _accessCard(clue):
    for card in deck:
        if card.clue.strip().upper() == clue.strip().upper():   
            return card
    return None

def printStats(clue):
    try:
        card = _accessCard(clue)
        print card.clue.upper()
        print 'Correct: %d, Incorrect: %d, Peeks: %d' %(card.correct, card.incorrect, card.peeks)
    except:
        print '%s is not in the deck.' %(clue.upper())

try:
    file_name = sys.argv[1] #prefix of the file that contains the deck
    if len(sys.argv[1:]) > 1:
        lookup_cards = sys.argv[2:] #get the clues of all cards for stat lookup
    else:
        lookup_cards = []
except:
    lookup_cards = []
    file_name = raw_input('Enter a .txt file name without the extension: ')
pickle_file_name = file_name+'_deck.txt'

## Update the deck with any new cards that may have been added
brand_new_deck = DeckReader.createDeck(file_name+'.txt')
new_cards = []
removed_cards = []

try:
    with open(pickle_file_name, 'rb') as f:
        try:
            deck = pickle.load(f)
            print 'Loaded old deck'
            for brand_new_card in brand_new_deck:
                same = False
                for card in deck:
                    if brand_new_card.clue == card.clue:
                        same = True
                if not same: #card has been added since deck was last played
                    deck.append(brand_new_card)
                    new_cards.append(brand_new_card)
                    
            for card in deck:
                same = False
                for brand_new_card in brand_new_deck:
                    if card.clue == brand_new_card.clue:
                        same = True
                if not same: #card is no longer in the modified deck
                    deck.remove(card)
                    removed_cards.append(card)
                    
            if new_cards:
                print 'New cards:'
                for nc in new_cards:
                    print '\t%s' %(nc.clue)
            if removed_cards:
                print 'Removed cards:'
                for rc in removed_cards:
                    print '\t%s' %(rc.clue)
               
        except: #deck failed to load
            deck = DeckReader.createDeck(file_name+'.txt')
            print 'Deck failed to load. Created new deck.'
except: #deck file doesn't exist
    deck = DeckReader.createDeck(file_name+'.txt')
    print 'File not found. Created new deck.'

if lookup_cards:
    for luc in lookup_cards:
        print '-'*10
        printStats(luc)
    print '\n'
    sys.exit(1)

num_items = len(deck)
    
print 'Enter <QUIT> to close the program.'
print 'Enter <PEEK> to see the answer.'

num_attempts = 0
num_correct = 0
num_peeks = 0

limit = 0
while limit < 1 or limit > num_items:
    limit = input('Enter the number of cards you want to see (maximum of %s): ' %(str(len(deck))))
sample = random.sample(deck, limit)

for card in sample:
    response = raw_input(card.clue+'? ')
    if response.upper() == 'QUIT':
        output = open(file_name+'_deck.txt', 'wb')
        try:
            pickle.dump(deck, output)
            print 'Pickled successfully'
        except:
            print 'Failed to pickle'
        output.close()
        break
    elif response.upper() == 'PEEK':
        card.peeks += 1
        num_peeks += 1
        print 'The answer is', card.answers[0].upper() + '.\n'
    else:
        num_attempts += 1
        if response.upper() in card.answers:
            card.correct += 1
            num_correct += 1
            print "Correct! Nice job.\n"
        else:
            card.incorrect += 1
            print "Incorrect. The correct answer is %s.\n" %(card.answers[0].title())

output = open(pickle_file_name, 'wb')
try:
    pickle.dump(deck, output)
    print 'Pickled successfully'
except:
    print 'Pickling failed'
output.close()

print '-'*20
print '-'*20

#results are written as ATTEMPTS    CORRECT    PEEKS
if num_attempts >= 0:
    results_file = file_name+'_results.txt'
    with open(results_file, 'a') as myfile:
        stats = [str(num_attempts), str(num_correct), str(num_peeks)]
        myfile.write('\t'.join(stats) + '\n')
    myfile.close()
raw_input('Press <ENTER> to see results')
print '\n'

# gather cumulative results for the deck just used
stats = TabulateResults.tabulate(results_file)
attempts, correct, peeks = stats

print '%d correct of %d attempts.\n' %(num_correct, num_attempts)
print "\nCUMULATIVE RESULTS FOR THIS DECK"
print '%d correct of %d attempts (%s peeks)' %(correct, attempts, peeks)
if attempts > 0:
    print '{percent:.2%}'.format(percent=1.0*correct/attempts), "accuracy\n" #change the 2 to adjust precision
raw_input('Press <ENTER> to end')
