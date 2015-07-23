# Flashcard Viewer

import pickle
import random
import sys

import DeckReader
import TabulateResults

def _get_card_by_clue(clue):
	for card in deck:
		if card.clue.upper() == clue.strip().upper():
			return card
	return None

def _get_stats_by_clue(clue):
	card = _get_card_by_clue(clue)
	if card != None:
		return (card.correct, card.incorrect, card.peeks)
	else:
		return None

def _check_file_exists(filename):
	pass

def print_cards(card_list):
	for card in card_list:
		print( '\t{}'.format(card.clue) )

def print_answer(card):
	print( 'The answer is {}.\n'.format(card.answers[0].upper()) )

def print_instructions():
	print( 'Enter <QUIT> to close the program.' )
	print( 'Enter <PEEK> to see the answer.' )

def get_deck_name():
	return input( 'Which deck would you like to use? ' )

def get_num_cards_this_session(minimum, maximum):
	limit = 0
	while limit < minimum or limit > maximum:
		limit = input( 'How many cards would you like to see? (between {} and {}) '.format(minimum, maximum) )
		try:
			limit = int(limit)
		except:
			limit = 0
	return limit

def _parse_args(args):
	pass

def play_card(card, session_stats):
	response 			= input( '{}? '.format(card.clue) ).upper()
	continue_playing 	= True
	if response == 'QUIT':
		continue_playing = False
	elif response == 'PEEK':
		card.peeks += 1
		session_stats['peeks'] += 1
		print_answer(card)
	else:
		session_stats['attempts'] += 1
		if response in card.answers:
			card.correct += 1
			session_stats['correct'] += 1
		else:
			card.incorrect += 1
			session_stats['incorrect'] += 1
			print_answer(card)
	return session_stats, continue_playing

def load_and_update_deck(pickle_filename, deck_filename):
	if not _check_file_exists( pickle_filename ):
		pass
	if not _check_file_exists( deck_filename ):
		pass

	try:
		with open( pickle_filename, 'rb' ) as pickle_file, open( deck_filename, 'rb' ) as deck_file:
			pickled_deck	= pickle.load( pickle_file )
			deck			= DeckReader.create_deck( deck_file.readlines() )
			common_cards 	= set([card for card in pickled_deck if card.clue in set([pcard.clue for pcard in pickled_deck]) & set([dcard.clue for dcard in deck])])
			new_cards 		= set([card for card in deck if card.clue in set([dcard.clue for dcard in deck]) - set([pcard.clue for pcard in pickled_deck])])
			removed_cards 	= set([card for card in pickled_deck if card.clue in set([pcard.clue for pcard in pickled_deck]) - set([dcard.clue for dcard in deck])])
	except:
		# use the provided file as the source of a brand new deck
		try:
			with open( deck_filename, 'rb' ) as deck_file:
				deck            = DeckReader.create_deck( deck_file.readlines() )
				common_cards 	= []
				new_cards		= deck
				removed_cards 	= []
		except:
			deck            = []
			common_cards 	= []
			new_cards		= []
			removed_cards 	= []
			print( 'Could not find that deck.....' )
			sys.exit( 1 )

	return (deck, common_cards, new_cards, removed_cards)

def pickle_deck(deck, pickle_filename):
	with open( pickle_filename, 'wb' ) as output:
		try:
			pickle.dump( deck, output )
		except:
			print( 'Could not pickle deck.' )

def write_results(session_stats, results_filename):
	with open( results_filename, 'a' ) as results_file:
		try:
			stats = [ session_stats['attempts'], session_stats['correct'], session_stats['incorrect'], session_stats['peeks'] ]
			results_file.write( '{}\n'.format('\t'.join([str(stat) for stat in stats])) )
		except:
			print( 'Could not write results to file.' )

def print_results(stats, session_stats):
	print( '{} correct of {} attempts.\n'.format(session_stats['correct'], session_stats['attempts']) )
	print( 'CUMULATIVE RESULTS FOR THIS DECK' )
	print( '{} correct of {} attempts ({} peeks)'.format(stats['correct'], stats['attempts'], stats['peeks']) )
	if stats['attempts'] > 0:
		print( '{percent:.2%}'.format(percent=1.0*stats['correct']/stats['attempts']) )

def main():
	deck_name 			= get_deck_name()
	deck_filename 		= './Decks/{}.txt'.format(deck_name)
	pickle_filename 	= './Pickles/{}_pickled.txt'.format(deck_name)
	results_filename	= './Results/{}_results.txt'.format(deck_name)

	[deck, common_cards, new_cards, removed_cards] = load_and_update_deck( pickle_filename, deck_filename )

	if new_cards:
		print( 'New cards:' )
		print_cards( new_cards )
	if removed_cards:
		print( 'Removed cards:' )
		print_cards( removed_cards )
	
	print()
	print_instructions()
	print()

	deck_size = len( deck )
	num_cards = get_num_cards_this_session( 1, deck_size )

	session 			= random.sample( deck, num_cards )
	session_stats 		= { 'attempts' : 0, 'correct' : 0, 'incorrect' : 0, 'peeks' : 0 }
	continue_playing 	= True
	for card in session:
		if continue_playing:
			session_stats, continue_playing = play_card( card, session_stats )

	pickle_deck( deck, pickle_filename )
	write_results( session_stats, results_filename )

	input( '\nPress <ENTER> to see results' )

	stats = TabulateResults.tabulate( results_filename )
	print_results( stats, session_stats )

	input( 'Press <ENTER> to end' )
	print()


if __name__ == '__main__':
	main()