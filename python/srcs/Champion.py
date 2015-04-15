import random


# genetic settings
RATIOS = {
    'add': 1,
    'delete': 1,
    'modify': 1,
    'pass': 1
}
TOTAL_RATIO = sum(RATIOS.values())

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

        if param == REG:
            return self.generate_register()
        if param == DIR:
            return self.generate_direct()
        if param == IND:
            return self.generate_indirect()

        raise ValueError('param should be either REG, DIR or IND')

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

    def mutate_instruction(self, instruction):

        pass

    def remove_instruction(self):

        pass

    def add_instruction(self, append = True):

        if append == True:
            self.data.update(self.generate_instruction())
        else:
            r = random.randint(0, 1) ##

    def mutate(self):

        r = random.randint(1, TOTAL_RATIO)
        if r < RATIOS['add']:
            self.add_instruction(False)
            return
        else:
            r = r - RATIOS['add']
        if r < RATIOS['delete']:
            self.delete_instruction()
            return
        else:
            r = r - RATIOS['delete']
        if r < RATIOS['modify']:
            self.modify_instruction()

    def generate(self, nb):

        for i in range(nb):
            self.data.append(self.generate_instruction()) # use add_instruction , add index

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
