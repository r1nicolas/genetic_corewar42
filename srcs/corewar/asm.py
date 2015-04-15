import subprocess

def assemble(asm, champion):

    p = subprocess.Popen([asm, champion])
    status = p.wait()
    return not status
