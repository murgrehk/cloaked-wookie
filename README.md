Seth Ebner

To use the Flashcard Viewer:

1. Download the ZIP file
2. Run `python3 fcv.py` from the command line
3. When prompted, enter the name of the `.txt` file containing the deck you want to play (leave off the `.txt` extension) and the number of cards you want to play

Note:
- You may quit answering cards at any time by entering `QUIT` as your answer
- You may see the answer without a penalty by entering `PEEK` as your answer
- The information displayed next to the clue corresponds to the number of times the card was answered correctly, incorrectly, or peeked. LS states how many sessions ago the card was last seen

To add a deck:

1. Create a `.txt` file in the `Decks` directory

To add cards to a deck:

1. Open the `.txt` file corresponding to the deck
2. Add the card’s clue and answers on a new line, following the format

	`CLUE; ANSWER_1, ANSWER_2`

3. Save the file

Note:
- Answers in the deck file are separated by commas, and the preferred answer is given first
- Upon using the modified deck, the Flashcard Viewer should note any cards that were added or removed
