import subprocess

def fight(corewar, champions):

    champions.insert(0, corewar)
    p = subprocess.Popen(champions, stdout = subprocess.PIPE)
    output, err = p.communicate()
    
