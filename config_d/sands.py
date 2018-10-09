def sands(keymap):
    """
    Space and Shift
    """
    keymap_global = keymap.defineWindowKeymap()
    keymap.replaceKey('Space', 'RShift')
    keymap_global['O-RShift'] = 'Space'
    keymap_global['O-LShift'] = 'Escape'
