# Card

## A flashcard object

class Card(object):

    def __init__(self, clue, answers, correct=0, incorrect=0, peeks=0):
        self.clue = clue
        self.answers = answers
        self.correct = 0
        self.incorrect = 0
        self.peeks = 0
