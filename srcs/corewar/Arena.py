from constants import *
import asm
import corewar
import os


class Arena:

    def __init__(self, corewar_path, asm, working_dir):

        self.corewar_path = corewar_path
        self.asm = asm
        self.working_dir = working_dir

    def build(self, target):

        res = asm.assemble(self.asm, target)
        if not res:
            return False

    def get_winner(self, a, b):

        return corewar.fight(self.corewar_path, [a, b])

    
