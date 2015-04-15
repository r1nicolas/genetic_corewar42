#!/usr/bin/python

from corewar.Champion import Champion

if __name__ == '__main__':

    c = Champion()
    c.generate(12)
    print c
    c.mutate()
    c.mutate()
    c.mutate()
    c.mutate()
    c.mutate()
    print c
