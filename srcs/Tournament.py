import math
import random

class Tournament(object):

    def __init__(self, elements = []):

        self.elements = self.init_elements(elements)

    @staticmethod
    def init_elements(elements):

        return [[i, 0] for i in elements]

    def fight(self, a, b):

        raise NotImplementedError

    def run(self):

        for i in xrange(len(self.elements)):
            for j in xrange(len(self.elements)):
                if not i == j:
                    if self.fight(self.elements[i][0], self.elements[j][0]) == 1:
                        self.elements[i][1] += 1
                    else:
                        self.elements[j][1] += 1

        return sorted(self.elements, key = lambda x: x[1])
