import subprocess

def fight(corewar, champions):

    """
    params:
    corewar: path to corewar binary
    champions: list of path to assembled champions
    return value: id of the winner champion
    """

    champions.insert(0, corewar)
    p = subprocess.Popen(champions, stdout = subprocess.PIPE)
    output, err = p.communicate()
    status = p.wait()
    if status == 44 or 43:
        return status - 42

    raise Exception, 'CorewarFail'
