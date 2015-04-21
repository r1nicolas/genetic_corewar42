from constants import *
import random

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
            'add': 3,
            'remove': 3,
            'mutate': 5,
            'pass': 2,
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

        if index == len(self.data):
            index = index - 1

        r = random.randint(0, len(self.data[index][1]) - 1)
        self.data[index][1][r][1] = self.generate_by_param(self.data[index][1][r][0])[1]

    def remove_instruction(self, index = 0):

        if len(self.data) == 1:
            return

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
            if r <= self.ratios[i]:
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
