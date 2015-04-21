import subprocess

def assemble(asm, champion):

    p = subprocess.Popen([asm, champion], stdout = subprocess.PIPE)
    status = p.wait()
    return not status
