# 2015.04.15 17:05:16 CEST

import random


MEM_SIZE = 4096
REG_NUMBER = 16

DIRECT_CHAR = '%'
REGISTER_CHAR = 'r'

REG = 0
DIR = 1
IND = 2

INSTRUCTIONS = {'live': [[DIR]],
 'ld': [[DIR, IND], [REG]],
 'st': [[REG], [REG, IND]],
 'add': [[REG], [REG], [REG]],
 'sub': [[REG], [REG], [REG]],
 'and': [[REG, DIR, IND], [REG, DIR, IND], [REG]],
 'or': [[REG, DIR, IND], [REG, DIR, IND], [REG]],
 'xor': [[REG, DIR, IND], [REG, DIR, IND], [REG]],
 'zjmp': [[DIR]],
 'ldi': [[REG, DIR, IND], [REG, DIR], [REG]],
 'sti': [[REG], [REG, DIR, IND], [REG, DIR]],
 'fork': [[DIR]],
 'lld': [[DIR, IND], [REG]],
 'lldi': [[REG, DIR, IND], [REG, DIR], [REG]],
 'lfork': [[DIR]],
 'aff': [[REG]]}

INSTRUCTIONS_LIST = INSTRUCTIONS.keys()


class Champion:

    def __init__(self, name = 't', comment = 't'):

        self.data = {}
        self.name = name
        self.comment = comment

    @staticmethod
    def generate_register():

        return [REG, random.randint(1, REG_NUMBER + 1)]

    @staticmethod
    def generate_direct():

        return [DIR, random.randint(0, MEM_SIZE)]

    @staticmethod
    def generate_indirect():

        return [IND, random.randint(0, MEM_SIZE)]

    def generate_by_param(self, param):

        if param == REG:
            return self.generate_register()
        if param == DIR:
            return self.generate_direct()
        if param == IND:
            return self.generate_indirect()

    def generate_instruction(self):

        r = random.randint(0, len(INSTRUCTIONS_LIST) - 1)
        op = INSTRUCTIONS_LIST[r]
        instruction = {op: []}
        for i in INSTRUCTIONS[op]:
            r = random.randint(0, len(i) - 1)
            p = i[r]
            res = self.generate_by_param(p)
            instruction[op].append(res)

        return instruction

    def mutate_instruction(self, instruction):

        pass

    def mutate(self):

        pass

    def generate(self, nb):

        for i in range(nb):
            self.data.update(self.generate_instruction())

    def __str__(self):

        s = '.name "{0}"\n.comment "{1}"\n\n'.format(self.name, self.comment)

        for i in self.data:
            s += '{0}\t'.format(i)
            for j in range(len(self.data[i])):
                if self.data[i][j][0] == REG:
                    s += REGISTER_CHAR
                elif self.data[i][j][0] == DIR:
                    s += DIRECT_CHAR
                s += str(self.data[i][j][1])
                if j != len(self.data[i]) - 1:
                    s += ', '

            s += '\n'

        return s
