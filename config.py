import time
from keyhac import *
import sys


def configure(keymap):
    keymap_global = keymap.defineWindowKeymap()

    # Enable oneshotmidifier Escape and LShift w/ any.
    keymap_global['O-LShift'] = 'Escape'

    # Enable oneshotmidifier Space and Shift w/ any.
    keymap.replaceKey('Space', 'RShift')
    keymap_global['O-RShift'] = 'Space'
    keymap_global['Cmd-RShift'] = 'Cmd-Space'

    # Enable Shift-Delete for forward delete.
    keymap_global['Shift-Back'] = 'Fn-Delete'

    # Enable onshotmidifier Semicolon and arrows w/ (h,j,k,l).
    keymap.replaceKey('Semicolon', '232')
    keymap_global['(232)'] = 'Semicolon'
    keymap_global['Shift-(232)'] = 'Shift-Semicolon'

    keymap.defineModifier('232', 'User0')
    for any in ("", "Ctrl-", "Alt-", "Alt-Ctrl-", "Cmd-", "Cmd-Ctrl-", "Cmd-Alt-", "Cmd-Alt-Ctrl-"):
        keymap_global[any + 'O-Shift-(232)'] = any + 'Colon'
        keymap_global[any + 'Shift-(232)'] = any + 'Semicolon'
        keymap_global[any + 'User0-h'] = any + 'Left'
        keymap_global[any + 'User0-j'] = any + 'Down'
        keymap_global[any + 'User0-k'] = any + 'Up'
        keymap_global[any + 'User0-l'] = any + 'Righ'
