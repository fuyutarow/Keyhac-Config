import time
from keyhac import *
import sys

from fakeymacs.config import configure as emacs_config
from config_d import (
    sands,
    # Vi,
    alias_launch_app,
    alt_英かな,
)
import config_d
print(dir(config_d))


def configure(keymap):
    emacs_config(keymap)
    sands(keymap)
    alt_英かな(keymap)
    alias_launch_app(keymap)
    #vi = Vi(keymap)
    #keymap_global['U0-x'] = vi.delete_char
    #keymap_global['U0-e'] = vi.kill_word

    ################################################################################
    # Move window
    ################################################################################
    keymap_global = keymap.defineWindowKeymap()
    keymap_global['A-C-h'] = 'W-C-Left'
    keymap_global['A-C-j'] = 'W-C-Down'
    keymap_global['A-C-k'] = 'W-C-Up'
    keymap_global['A-C-l'] = 'W-C-Right'
    keymap_global['A-S-h'] = 'W-Left'
    keymap_global['A-S-j'] = 'W-Down'
    keymap_global['A-S-k'] = 'W-Up'
    keymap_global['A-S-l'] = 'W-Right'
    keymap_global['A-t'] = 'C-t'  # new tab
    keymap_global['A-n'] = 'C-n'  # new window
    keymap_global['A-x'] = 'C-x'  # xut
    keymap_global['A-c'] = 'C-c'  # copy
    keymap_global['A-v'] = 'C-v'  # vast
    keymap_global['A-l'] = 'C-l'  # focus link
    keymap_global['A-f'] = 'C-f'  # find
    keymap_global['A-g'] = 'C-g'  # find
    keymap_global['A-w'] = 'C-w'  # owaru
    keymap_global['A-q'] = 'A-F4'  # quit
    keymap_global['A-C-f'] = 'W-up'  # quit
    keymap_global['W-A-h'] = 'W-Left'
    keymap_global['W-A-j'] = 'W-Down'
    keymap_global['W-A-k'] = 'W-Up'
    keymap_global['W-A-l'] = 'W-Right'

    ################################################################################
    # vim like
    ################################################################################
    keymap.defineModifier('Semicolon', 'User0')
    for any in ("", "S-", "C-", "C-S-", "A-", "A-S-", "A-C-", "A-C-S-", "W-",
                "W-S-", "W-C-", "W-C-S-", "W-A-", "W-A-S-", "W-A-C-",
                "W-A-C-S-"):
        # keymap_global[any + 'O-Space'] = any + 'Space'
        # keymap_global[any + 'O-Semicolon'] = any + 'Semicolon'
        # keymap_global[any + 'O-S-Semicolon'] = any + 'Colon'
        keymap_global[any + 'U0-h'] = any + 'Left'
        keymap_global[any + 'U0-j'] = any + 'Down'
        keymap_global[any + 'U0-k'] = any + 'Up'
        keymap_global[any + 'U0-l'] = any + 'Right'
        keymap_global[any + 'U0-q'] = any + 'Escape'
        keymap_global[any + 'U0-b'] = any + 'Back'
        keymap_global[any + 'U0-n'] = any + 'Return'
        keymap_global[any + 'U0-m'] = any + 'Return'
    from datetime import datetime
    now = datetime.now().strftime('%Y-%m-%d %H:%m:%S')
    keymap_global['U0-S-C-n'] = keymap.InputTextCommand(now)

    keymap_global['U0-S-a'] = 'End'
    keymap_global['U0-S-i'] = 'Home'
    keymap_global['U0-C-a'] = 'Home'
    keymap_global['U0-C-e'] = 'End'
    keymap_global['U0-o'] = 'End', 'S-Return'
    #keymap_global['U0-x'] = 'Delete'
    keymap_global['U0-S-x'] = 'Left', 'Delete'
    keymap_global['U0-S-o'] = 'Home', 'S-Return', 'Up'
    keymap_global['U0-S-d'] = 'S-End', 'Delete'
    keymap_global['U0-d'] = keymap.defineMultiStrokeKeymap('')
    keymap_global['U0-d']['U0-d'] = 'Home', 'S-End', 'C-x'

    #keymap_global['Escape'] = switch_ime(False), 'Escape'

    #greek_upper = {
    #    'alpha': 'Α',
    #    'beta': 'Β',
    #    'gamma': 'Γ',
    #    'delta': 'Δ',
    #    'epsilon': 'Ε',
    #    'zeta': 'Ζ',
    #    'eta': 'Η',
    #    'theta': 'Θ',
    #    'iota': 'Ι',
    #    'kappa': 'Κ',
    #    'lambda': 'Λ',
    #    'mu': 'Μ',
    #    'nu': 'Ν',
    #    'xi': 'Ξ',
    #    'omicron': 'Ο',
    #    'pi': 'Π',
    #    'rho': 'Ρ',
    #    'sigma': 'Σ',
    #    'tau': 'Τ',
    #    'upsilon': 'Υ',
    #    'phi': 'Φ',
    #    'chi': 'Χ',
    #    'psi': 'Ψ',
    #    'omega': 'Ω',
    #}
    #greek_lower = {
    #    'alpha': 'α',
    #    'beta': 'β',
    #    'gamma': 'γ',
    #    'delta': 'δ',
    #    'epsilon': 'ε',
    #    'zeta': 'ζ',
    #    'eta': 'η',
    #    'theta': 'θ',
    #    'iota': 'ι',
    #    'kappa': 'κ',
    #    'lambda': 'λ',
    #    'mu': 'μ',
    #    'nu': 'ν',
    #    'xi': 'ξ',
    #    'omicron': 'ο',
    #    'pi': 'π',
    #    'rho': 'ρ',
    #    'sigma': 'σ',
    #    'tau': 'τ',
    #    'upsilon': 'υ',
    #    'phi': 'φ',
    #    'chi': 'χ',
    #    'psi': 'ψ',
    #    'omega': 'ω',
    #}

    #entry_greek_upper = keymap_global['S-U0-LShift'] = keymap.defineMultiStrokeKeymap()
    #entry_greek_lower = keymap_global['U0-LShift'] = keymap.defineMultiStrokeKeymap()

    #def input_greek_alphabet(name, case):
    #    d = {'upper': entry_greek_upper, 'lower': entry_greek_lower}[case]
    #    s = ''
    #    for c in name[:-1]:
    #        s += c
    #        keymap.popBalloon('ime_status', s, 500)
    #        d[c] = keymap.defineMultiStrokeKeymap()
    #        d = d[c]
    #    d[name[-1]] = keymap.InputTextCommand({
    #        'upper': greek_upper[name],
    #        'lower': greek_lower[name]
    #    }[case])

    #for name in greek_upper.keys():
    #    input_greek_alphabet(name, 'upper')
    #    input_greek_alphabet(name, 'lower')
