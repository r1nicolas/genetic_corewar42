import math
import random

# self.elements = [ [champion, score, previous oponents], ...]

class Tournament(object):

    def __init__(self, elements = [], round_number = None):

        self.elements = self.init_elements(elements)
        random.shuffle(self.elements)
        if not self.round_number:
            self.round_number = self.get_round_number()

    @staticmethod
    def init_elements(elements):

        i = 0
        while i < len(elements):
            elements[i] = [i, 0, []]
            i += 1

        if len(elements) % 2:
            elements[i][1] = 1

    def get_round_number(self):

        return int(math.ceil(math.sqrt(len(self.elements))))

    def populate(self, elements):

        self.elements.append(elements)

    def run(self):

        if not getattr(self, 'fight'):
            raise 'Implementation error: you must implement the \'fight\' method.'

    def pair(self):

        # classer par score
        # matcher 2 par deux - ne pas fight le meme type
        # alterner joueur 1 / joueur 2
