def switch_ime(flag):
    BALLOON_TIMEOUT_MSEC = 500

    if flag:
        ime_status = 1
        message = u'[あ]'
    else:
        ime_status = 0
        message = u'[_A]'
    wnd = keymap.getTopLevelWindow()

    # keymap.wnd.getImeStatus()
    def wrap():
        keymap.wnd.setImeStatus(ime_status)
        keymap.popBalloon('ime_status', message, BALLOON_TIMEOUT_MSEC)

    return wrap


def alt_英かな(keymap):
    keymap_global = keymap.defineWindowKeymap()
    keymap_global['D-RAlt'] = 'D-RAlt', 'LCtrl'
    keymap_global['D-LAlt'] = 'D-LAlt', 'LCtrl'
    keymap_global['O-RAlt'] = switch_ime(True)
    keymap_global['O-LAlt'] = switch_ime(False)
