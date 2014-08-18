Seth Ebner
Created: 8-16-14
Last Modified: 8-18-14

To use the Flashcard Viewer:
	-install Python 2.7
	-copy all .py files and any .txt files from the repository into the same directory
	-navigate to the directory containing the files and run fcv.py from Command Prompt or Terminal
		-the deck may be specified as a command line argument, following the format

			python fcv.py deckname

		-the number of cards you want to play may also be entered as a command line argument following the name of the deck, following the format

			python fcv.py deckname number

	-if no command line arguments are given, when prompted, enter the name of the .txt file containing the deck you want to play (leave off the .txt extension) and the number of cards you want to play
	-you may quit answering cards at any time by entering QUIT
	-you may see the answer without a penalty by entering PEEK

To add a deck:
	-create a .txt file in the same directory as the rest of the files

To add cards to a deck:
	-open the .txt file corresponding to the deck
	-add the card’s clue and answers on a new line, following the format

		CLUE; ANSWERS

	-answers are separated by commas, and the preferred answer is given first
	-save the file
	-upon using the modified deck, the Flashcard Viewer should note any new cards that were added

To look up the statistics of a card:
	-run the Flashcard Viewer with the deck and the clue of any card in that deck as command line arguments, following the format (making sure the clues are in double-quotes)

		python fcv.py deckname “clue1” “clue2”

	-the statistics of any cards entered as command line arguments will be printed
