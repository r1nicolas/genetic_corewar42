#!/usr/bin/python

import os
import shutil
from corewar.Champion import Champion
from corewar.CTournament import CTournament
from corewar.constants import *
from corewar.asm import assemble


def compile_champions(asm_path, champions, working_dir):

    for i in xrange(len(champions)):
        s_path = '/tmp/' + champions[i].name + '.s'
        cor_path = '/tmp/' + champions[i].name + '.cor'
        dst_path = working_dir + champions[i].name + '.cor'

        with open(s_path, 'w') as fd:
            fd.write(str(champions[i]))

        assemble(asm_path, s_path)
        try:
            os.remove(dst_path)
        except:
            pass
        shutil.move(cor_path, working_dir)
        champions[i].cor_path = dst_path

def mutate_champions(res):

    for i in xrange(len(res)):
        if res[i][1] < 45:
            res[i][0].mutate()
        if res[i][1] < 31:
            res[i][0].mutate()
        if res[i][1] < 16:
            res[i][0].mutate()
        

if __name__ == '__main__':

    champions = [Champion(str(i)) for i in xrange(CHAMPIONS_NB)]
    for i in xrange(len(champions)):
        champions[i].generate(DEFAULT_SIZE)

    i = 0
    while True:
        compile_champions(ASM_PATH, champions, WORKING_DIR)
        t = CTournament(COREWAR_PATH, champions)
        res = t.run()
        mutate_champions(res)
        print 'gen : {0}'.format(str(i))
        print res[-1][0]
        print 'score : {0}'.format(str(res[-1][1]))
        print '#########################'
        champions = map(lambda x: x[0], res)
        i += 1

    # generate X champions
    #  A : compile them
    # let them fight
    # apply mutation rules - 10 % best -> no mutation ; 10 -> 90 % % -> 1 mutation ; 90 -> 100 % -> 2 mutations
    # goto A
