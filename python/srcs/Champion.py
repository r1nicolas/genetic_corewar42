import random


# genetic settings

# corewar rules
MEM_SIZE = 4096
REG_NUMBER = 16
CHAMP_MAX_SIZE = MEM_SIZE / 6

# asm specifications
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

        self.data = []
        self.name = name
        self.comment = comment
        self.generate_f = {
            REG: self.generate_register,
            DIR: self.generate_direct,
            IND: self.generate_indirect,
            }
        self.ratios = {
            'add': 1,
            'remove': 1,
            'mutate': 1,
            'pass': 1,
            }

    @staticmethod
    def generate_register():

        return [REG, random.randint(1, REG_NUMBER + 1)]

    @staticmethod
    def generate_direct():

        return [DIR, random.randint(0, MEM_SIZE)]

    @staticmethod
    def generate_indirect():

        return [IND, random.randint(0, MEM_SIZE)]

    @staticmethod
    def get_instruction_size():

        pass

    def generate_by_param(self, param):

        return self.generate_f[param]()

    def generate_instruction(self):

        r = random.randint(0, len(INSTRUCTIONS_LIST) - 1)
        op = INSTRUCTIONS_LIST[r]
        instruction = [op, []]
        for i in INSTRUCTIONS[op]:
            r = random.randint(0, len(i) - 1)
            p = i[r]
            res = self.generate_by_param(p)
            instruction[1].append(res)

        return instruction

    def mutate_instruction(self, index = 0):

        pass

    def remove_instruction(self, index = 0):

        if index == len(self.data):
            index = index - 1
        del self.data[index]

    def add_instruction(self, index = 0):

        self.data.insert(index, self.generate_instruction())

    def pass_instruction(self, index = 0):

        pass

    def mutate(self):

        r = random.randint(1, sum(self.ratios.values()))
        for i in self.ratios:
            if r < self.ratios[i]:
                m = getattr(self, '{0}_instruction'.format(i))
                m(random.randint(0, len(self.data)))
                return
            r -= self.ratios[i]

    def generate(self, nb):

        for i in range(nb):
            self.add_instruction(i)

    def __str__(self):

        s = '.name "{0}"\n.comment "{1}"\n\n'.format(self.name, self.comment)

        for i in self.data:
            s += '{0}\t'.format(i[0])
            for j in range(len(i[1])):
                if i[1][j][0] == REG:
                    s += REGISTER_CHAR
                elif i[1][j][0] == DIR:
                    s += DIRECT_CHAR
                s += str(i[1][j][1])
                if j != len(i[1]) - 1:
                    s += ', '
            s += '\n'

        return s
