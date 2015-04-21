# genetic settings
CHAMPIONS_NB = 2 ** 5
DEFAULT_SIZE = 4

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
                'aff': [[REG]]
                }

INSTRUCTIONS_LIST = INSTRUCTIONS.keys()

# misc
WORKING_DIR = '/nfs/zfs-student-5/users/2013/aguilbau/documents/corewar/genetic_corewar42/run/'
COREWAR_PATH = '/nfs/zfs-student-5/users/2013/aguilbau/documents/corewar/corewar'
ASM_PATH = '/nfs/zfs-student-5/users/2013/aguilbau/documents/corewar/asm'
