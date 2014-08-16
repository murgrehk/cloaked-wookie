# Flashcard

import random
import DeckReader
import TabulateResults
import pickle
import sys

def accessCard(clue):
    for card in deck:
        if card.clue.upper() == clue.upper():
            return card
    return None

def printStats(clue):
    card = accessCard(clue)
    print '%s: %s' %(card.clue, card.answers[0])
    print 'Correct: %d, Incorrect: %d, Peeks: %d' %(card.correct, card.incorrect, card.peeks)

##def countLines(file_name):
##    non_blank_count = 0
##
##    with open(file_name+'.txt') as infp:
##        for line in infp:
##           if line.strip():
##              non_blank_count += 1

file_name = raw_input('Enter a .txt file name without the extension: ')
pickle_file_name = file_name+'_deck.txt'

## Update the deck with any new cards that may have been added
brand_new_deck = DeckReader.createDeck(file_name+'.txt')

try:
    with open(pickle_file_name, 'rb') as f:
        try:
            deck = pickle.load(f)
            print 'Loaded old deck'
            if len(brand_new_deck) > len(deck):
                for brand_new_card in brand_new_deck:
                    same = False
                    for card in deck:
                        if brand_new_card.clue == card.clue:
                            same = True
                    if not same: #card has been added since deck was last played
                        deck.append(brand_new_card)
                        print brand_new_card.clue
                print 'New cards loaded into deck'
        except: #deck failed to load
            deck = DeckReader.createDeck(file_name+'.txt')
            print 'Created new deck'
except: #deck file doesn't exist
    deck = DeckReader.createDeck(file_name+'.txt')
    print 'Created new deck kjdhfksd f'

num_items = len(deck)
    
print 'Enter <QUIT> to close the program.'
print 'Enter <PEEK> to see the answer.'

num_attempts = 0
num_correct = 0
num_peeks = 0

limit = 0
while limit < 1 or limit > num_items:
    limit = input('Enter the number of cards you want to see (maximum of %s): ' %(str(num_items)))
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
