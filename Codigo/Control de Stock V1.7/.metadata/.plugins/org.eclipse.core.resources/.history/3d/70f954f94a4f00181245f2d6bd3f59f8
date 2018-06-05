import subprocess as sp
import sys


def limpia():
    plataforma = sys.platform
    if plataforma.startswith('linux'):
        sp.call('clear')
    elif plataforma.startswith('win'):
        sp.call('cls', shell=True)