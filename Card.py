#Card

class Card(object):

    def __init__(self, clue, answers):
        self.clue = clue
        self.answers = answers
        self.correct = 0
        self.incorrect = 0
        self.peeks = 0
