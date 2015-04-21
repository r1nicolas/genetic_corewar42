import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
from Tournament import Tournament
import corewar

class CTournament(Tournament):

    def __init__(self, corewar_path, *args, **kwargs):

        super(CTournament, self).__init__(*args, **kwargs)
        self.corewar_path = corewar_path

    def fight(self, a, b):

        return corewar.fight(self.corewar_path, [a.cor_path, b.cor_path])
