import time
from keyhac import *
import sys


def configure(keymap):
    keymap_global = keymap.defineWindowKeymap()
    keymap.replaceKey('Space', 'RShift')
    keymap_global['O-RShift'] = 'Space'
    keymap_global['Cmd-RShift'] = 'Cmd-Space'
    keymap_global['O-LShift'] = 'Escape'
