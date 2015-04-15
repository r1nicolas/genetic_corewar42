#!/usr/bin/python

import random
import pprint

"""

{"operande1": [[type,arg1], [type,arg2], ..], "operande2": [...], ...}

"""


REG_NUMBER = 16

REG = 0
DIR = 1
IND = 2

INSTRUCTIONS = {
    'live': [[DIR]],
    'ld': [[DIR, IND], [REG]],
    'st': [[REG, IND], [REG]],
    'add': [[REG], [REG], [REG]],
    'sub': [[REG], [REG], [REG]],
    'and': [[REG, DIR, IND], [REG, DIR, IND], [REG]],
    'or': [[REG, DIR, IND], [REG, DIR, IND], [REG]],
    'xor': [[REG, DIR, IND], [REG, DIR, IND], [REG]],
    'zjmp': [[DIR]],
    'ldi': [[REG, DIR, IND], [REG, DIR], [REG]],
    'sti': [[REG], [REG, DIR, IND], [REG, DIR]],
    'fork': [[DIR]],
    'lld': [[DIR]],
    'lldi': [[REG, DIR, IND], [REG, DIR], [REG]],
    'lfork': [[DIR]],
    'aff': [[REG]],
}

INSTRUCTIONS_LIST = INSTRUCTIONS.keys()

def generate_register():

    return [REG, random.randint(1, REG_NUMBER + 1)]

def generate_direct():

    return [DIR, random.randint(1, 4294967296)]

def generate_indirect():

    return [IND, random.randint(1, 4294967296)]

GEN_PARAM_F = {
    REG: generate_register,
    DIR: generate_direct,
    IND: generate_indirect
}

def generate_by_param(param):

    return GEN_PARAM_F[param]()

def generate_instruction():

    # choose a random instruction -> op
    r = random.randint(0, len(INSTRUCTIONS_LIST) - 1)
    op = INSTRUCTIONS_LIST[r]

    instruction = {op: []}

    # for each arg, generate a random value
    for a in INSTRUCTIONS[op]:
        r = random.randint(0, len(a) - 1)
        p = a[r]
        res = generate_by_param(p)
        instruction[op].append(res)

    return instruction

def mutate_instruction(i):

    raise NotImplementedError

if __name__ == '__main__':

    res = {}

    r = random.randint(1, 18)
    for i in range(r):
        res.update(generate_instruction())

    pprint.pprint(res)
