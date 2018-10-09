def launch_ubuntu():
    #shellExecute(None, "ubuntu.exe", "", "")
    shellExecute(None, "ubuntu1804.exe", "", "")


def launch_edge():
    shellExecute(None, None, "start", "microsoft-edge:", "")


def alias_launch_app(keymap):
    keymap_global = keymap.defineWindowKeymap()
    keymap_global['U0-t'] = launch_ubuntu
    keymap_global['U0-e'] = launch_edge
